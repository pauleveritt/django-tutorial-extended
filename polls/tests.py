import pytest


@pytest.mark.django_db
def test_adding_new_question(question, api_client):
    payload = {
        "question_text": question.question_text,
        "pub_date": str(question.pub_date)
    }

    response = api_client.post("/v1/question/", payload)
    assert response.status_code == 201
