from django.db import models
from django.db.models import F, Value
from django.db.models.functions import Lower, Now, Replace


class Article(models.Model):
    created_at = models.DateTimeField(db_default=Now())
    title = models.CharField(max_length=300)
    slug = models.GeneratedField(
        expression=Lower(Replace(F("title"), Value(" "), Value("-"))),
        db_persist=True,
        unique=True,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("blog:detail", kwargs={"slug": self.slug})
