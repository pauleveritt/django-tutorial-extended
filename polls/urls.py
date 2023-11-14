from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("add/", views.add_question, name="add"),
    path("add-choice/", views.add_choice, name="add_choice"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
