import datetime

from django.contrib import admin
from django.db import models
from django.db.models import F
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    closed_date = models.DateTimeField("date closed", null=True)
    poll_duration = models.GeneratedField(
        expression=F("closed_date") - F("pub_date"),
        db_persist=True,
    )

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="choices"
    )
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(db_default=0)

    def __str__(self):
        return self.choice_text
