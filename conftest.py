import pytest
from django.utils import timezone

from polls.models import Question
from rest_framework.test import APIClient


@pytest.fixture
def question():
    question_obj = Question.objects.create(question_text="Hello, this is a sample text !",
                                           pub_date=timezone.now())
    return question_obj


@pytest.fixture
def api_client():
    return APIClient()
