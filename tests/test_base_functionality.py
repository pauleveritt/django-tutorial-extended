import json

import pytest
import requests
from bs4 import BeautifulSoup

from conftest import QUESTION_TEXT


@pytest.mark.django_db
def test_polls_index(client, question):
    # The question fixture above causes the dummy db to get populated

    # Use a non-server TestClient to issue request, get response
    response = client.get("/polls/")

    # Get at the view's context data, meaning, query result
    rows = response.context_data["object_list"]
    assert len(rows) > 0

    # Test the base template's rendering
    html = BeautifulSoup(response.content, "html5lib")
    avatar = html.select_one("#avatar")
    assert avatar["src"] == "/static/polls/images/man.png"

    # Make sure we rendered a question
    question_texts = html.select(".question_text")
    assert question_texts[0].text == QUESTION_TEXT


def get_html_document(url):
    # request for HTML document of given url
    response = requests.get(url)

    # response will be provided in JSON format
    return response.text


@pytest.mark.django_db
def test_adding_new_question(api_client):
    payload = {
        "question_text": "This is a sample question",
        "pub_date": "2022-01-01",
        "choices": [
            {
                "choice_text": "Choice 1"
            },
            {
                "choice_text": "Choice 2"
            },
            {
                "choice_text": "Choice 3"
            },
            {
                "choice_text": "Choice 4"
            }
        ]
    }
    payload = json.dumps(payload)
    response = api_client.post("/v1/question/", payload, content_type="application/json")
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


@pytest.mark.django_db
def test_image_exist_in_the_page(question, api_client):
    # Fetch Data from URL
    url_to_scrape = "http://localhost:8000/polls/"

    # create document
    html_document = get_html_document(url_to_scrape)

    # create soap object
    soup = BeautifulSoup(html_document, 'html.parser')
    images = soup.findAll('img')
    images_list = list()
    for image in images:
        images_list.append(str(image['src']).split("/")[-1])

    image_exist = "PyCharm.svg" in images_list
    assert image_exist is True
