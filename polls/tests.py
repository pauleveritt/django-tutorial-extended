from datetime import datetime, timedelta, timezone

from django.test import TestCase
from django.urls import reverse

from polls.models import Choice, Question


class PollsDataTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.question_cats_dogs = Question.objects.create(
            question_text="Cats or Dogs?",
            pub_date=datetime(2003, 1, 1, tzinfo=timezone.utc),
            closed_date=datetime(2003, 1, 3, tzinfo=timezone.utc),
        )
        cls.question_coffee_tea = Question.objects.create(
            question_text="Coffee or Tea?",
            pub_date=datetime(2005, 1, 1, tzinfo=timezone.utc),
        )
        cls.choice_coffee = Choice.objects.create(
            question=cls.question_coffee_tea, choice_text="Coffee"
        )
        cls.choice_tea = Choice.objects.create(
            question=cls.question_coffee_tea, choice_text="Tea"
        )


class ModelTests(PollsDataTestCase):
    def test_question_duration(self):
        self.assertEqual(self.question_cats_dogs.poll_duration, timedelta(days=2))
        self.assertIsNone(self.question_coffee_tea.poll_duration)

    def test_string_method(self):
        self.assertEqual(str(self.question_cats_dogs), "Cats or Dogs?")
        self.assertEqual(str(self.question_coffee_tea), "Coffee or Tea?")
        self.assertEqual(str(self.choice_coffee), "Coffee")
        self.assertEqual(str(self.choice_tea), "Tea")


class PollNoDataViews(TestCase):
    def test_index_view_no_data(self):
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "polls/index.html")
        self.assertContains(response, "No polls are available.")

    def test_detail_view_not_found(self):
        response = self.client.get(reverse("polls:detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, 404)

    def test_vote_view_found(self):
        response = self.client.get(reverse("polls:vote", kwargs={"question_id": 1}))
        self.assertEqual(response.status_code, 404)


class PollsViewsData(PollsDataTestCase):
    def test_index_view_data(self):
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "polls/index.html")
        self.assertContains(response, self.question_cats_dogs.question_text)
        self.assertContains(response, self.question_coffee_tea.question_text)
        self.assertContains(response, self.choice_tea.choice_text)
        self.assertContains(response, self.choice_coffee.choice_text)

    def test_detail_view_found(self):
        response = self.client.get(
            reverse("polls:detail", kwargs={"pk": self.question_coffee_tea.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "polls/detail.html")
        self.assertContains(response, self.question_coffee_tea.question_text)
        self.assertContains(response, self.choice_tea.choice_text)
        self.assertContains(response, self.choice_coffee.choice_text)

    def test_vote(self):
        self.assertEqual(self.choice_tea.votes, 0)
        response = self.client.post(
            reverse("polls:vote", kwargs={"question_id": self.question_coffee_tea.id}),
            data={"choice": self.choice_tea.id},
        )
        self.assertEqual(response.status_code, 302)
        self.choice_tea.refresh_from_db()
        self.assertEqual(self.choice_tea.votes, 1)
