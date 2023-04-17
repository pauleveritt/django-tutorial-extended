import pytest
from django.utils import timezone
from rest_framework.test import APIClient

from polls.models import Question

QUESTION_TEXT = "Hello, this is a sample text !"


@pytest.fixture
def question():
    question_obj = Question.objects.create(question_text=QUESTION_TEXT,
                                           pub_date=timezone.now())
    return question_obj


@pytest.fixture
def api_client():
    return APIClient()
