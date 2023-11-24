from django import forms

from utils.forms import BaseForm


class AddQuestionForm(BaseForm):
    question_text = forms.CharField(label="Question", max_length=100)


class AddChoiceForm(BaseForm):
    choice_text = forms.CharField(
        label="Choice",
        max_length=200,
        template_name="snippets/field.html",
    )
