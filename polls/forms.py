from django import forms


class AddQuestionForm(forms.Form):
    question_text = forms.CharField(label="Question", max_length=100)
    closed_date = forms.DateField(
        label="Poll closed at",
        widget=forms.SelectDateWidget,
        required=False,
    )


class AddChoiceForm(forms.Form):
    choice_text = forms.CharField(
        label="Choice",
        max_length=200,
        template_name="snippets/field.html",
    )
