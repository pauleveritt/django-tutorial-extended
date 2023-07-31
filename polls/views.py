from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone

from .models import Choice, Question


def index_view(request):
    template_name = "polls/index.html"
    latest_question_list = Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")

    return render(request, template_name, {'latest_question_list': latest_question_list})


def detail_view(request, pk):
    template_name = "polls/detail.html"

    question = get_object_or_404(Question, pk=pk, pub_date__lte=timezone.now())

    return render(request, template_name, {'question': question})


def results_view(request, pk):
    template_name = "polls/results.html"

    question = get_object_or_404(Question, pk=pk)

    return render(request, template_name, {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
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
