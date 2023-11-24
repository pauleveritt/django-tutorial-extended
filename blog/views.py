from django.views import generic

from blog.models import Article


class IndexView(generic.ListView):
    template_name = "blog/index.html"
    context_object_name = "article_list"

    def get_queryset(self):
        return Article.objects.all()


class DetailView(generic.DetailView):
    model = Article
    template_name = "blog/detail.html"
