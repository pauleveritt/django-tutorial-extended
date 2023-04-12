import pytest
from django.utils import timezone


@pytest.mark.django_db
def test_adding_new_question(api_client):
    payload = {
        "question_text": "This is a dummy text",
        "pub_date": timezone.now()
    }

    response = api_client.post("/v1/question/", payload)
    assert response.status_code == 201


@pytest.mark.django_db
def test_list_question_by_id(question, api_client):
    response = api_client.get(f"/v1/question/{question.id}")
    assert response.status_code == 200
    assert response.data["question_text"] == "Hello, this is a sample text !"


@pytest.mark.django_db
def test_delete_question_by_id(question, api_client):
    response = api_client.delete(f"/v1/question/{question.id}")
    assert response.status_code == 204
