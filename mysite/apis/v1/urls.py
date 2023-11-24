from django.urls import path

from . import views

urlpatterns = [
    path("question/", views.QuestionAPI.as_view()),
    path("question/<int:pk>", views.QuestionRetrieveUpdateDestroyAPI.as_view()),
    path("vote/", views.ChoiceVoteAPI.as_view()),
]
