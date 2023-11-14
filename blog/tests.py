from django.test import TestCase
from django.urls import reverse

from blog.models import Article


class ArticleModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.article = Article.objects.create(title="Example title of article")

    def test_slug_field(self):
        self.assertEqual(self.article.slug, "example-title-of-article")

    def test_get_absolute_url(self):
        self.assertEqual(
            self.article.get_absolute_url(), "/blog/example-title-of-article/"
        )

    def test_string_method(self):
        self.assertEqual(str(self.article), "Example title of article")


class ArticleViews(TestCase):
    def test_index_view_no_data(self):
        response = self.client.get(reverse("blog:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/index.html")
        self.assertContains(response, "No articles are available.")

    def test_index_view_data(self):
        article_1 = Article.objects.create(title="Hello world")
        article_2 = Article.objects.create(title="Example title of article")
        response = self.client.get(reverse("blog:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/index.html")
        self.assertContains(response, article_1.get_absolute_url())
        self.assertContains(response, article_1.title)
        self.assertContains(response, article_2.get_absolute_url())
        self.assertContains(response, article_2.title)
        self.assertNotContains(response, "No articles are available.")

    def test_detail_view_not_found(self):
        response = self.client.get(
            reverse("blog:detail", kwargs={"slug": "hello-world"})
        )
        self.assertEqual(response.status_code, 404)

    def test_detail_view_found(self):
        Article.objects.create(title="Hello world")
        response = self.client.get(
            reverse("blog:detail", kwargs={"slug": "hello-world"})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/detail.html")
        self.assertContains(response, "Hello world")
