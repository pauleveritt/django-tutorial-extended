from django.forms import formset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .forms import AddQuestionForm, AddChoiceForm
from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date").select_related()[0:10]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).select_related()


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choices.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


def add_question(request):
    ChoiceFormSet = formset_factory(AddChoiceForm, extra=4)
    if request.POST:
        question_form = AddQuestionForm(request.POST)
        choice_formset = ChoiceFormSet(request.POST)
        if question_form.is_valid() and choice_formset.is_valid():
            new_question = Question.objects.create(
                question_text=question_form.cleaned_data["question_text"],
                pub_date=timezone.now(),
                closed_date=question_form.cleaned_data.get("closed_date"),
            )
            for choice_form in choice_formset:
                if "choice_text" in choice_form.cleaned_data:
                    Choice.objects.create(
                        question=new_question,
                        choice_text=choice_form.cleaned_data["choice_text"]
                    )
            return HttpResponseRedirect(reverse("polls:index"))
    else:
        question_form = AddQuestionForm()
        choice_formset = ChoiceFormSet()

    return render(
        request,
        template_name="polls/add.html",
        context={"question_form": question_form, "choice_formset": choice_formset}
    )
