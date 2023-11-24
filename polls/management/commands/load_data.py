from django.core.management.base import BaseCommand
from django.utils import timezone

from blog.models import Article
from polls.models import Choice, Question


class Command(BaseCommand):
    help = "Load Data to DB"

    def handle(self, *args, **kwargs):
        # Flush all data
        Question.objects.all().delete()
        Article.objects.all().delete()

        # Insert new questions
        question_one = Question.objects.create(
            question_text="How proficient you are working with PyCharm ?",
            pub_date=timezone.now(),
        )

        choices_one_list = [
            Choice(choice_text="I'm completely green", question_id=question_one.id),
            Choice(
                choice_text="I have some basic knowledge", question_id=question_one.id
            ),
            Choice(
                choice_text="I have some solid background", question_id=question_one.id
            ),
            Choice(choice_text="I'm an expert", question_id=question_one.id),
        ]

        question_two = Question.objects.create(
            question_text="The organization invests time and money to keep the employee updated with technology.",
            pub_date=timezone.now(),
        )

        choices_two_list = [
            Choice(choice_text="Agree", question_id=question_two.id),
            Choice(choice_text="Disagree", question_id=question_two.id),
            Choice(
                choice_text="Neither Agree nor Disagree", question_id=question_two.id
            ),
        ]

        question_three = Question.objects.create(
            question_text="What is you age ?", pub_date=timezone.now()
        )

        choices_three_list = [
            Choice(choice_text="Under 18", question_id=question_three.id),
            Choice(choice_text="18-24", question_id=question_three.id),
            Choice(choice_text="25-36", question_id=question_three.id),
            Choice(choice_text="Above 36", question_id=question_three.id),
        ]

        Choice.objects.bulk_create(choices_one_list)
        Choice.objects.bulk_create(choices_two_list)
        Choice.objects.bulk_create(choices_three_list)

        self.stdout.write("Questions loaded into DB")

        Article.objects.create(title="Hello world")
        Article.objects.create(title="2022 year in review")
        Article.objects.create(title="2023 year in review")
        Article.objects.create(title="Do blog articles make you smarter")

        self.stdout.write("Articles loaded into DB")
