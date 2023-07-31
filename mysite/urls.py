"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from mysite.apis.v1 import views as question_view
from polls import views as polls_view
urlpatterns = [
    path('', views.index_view, name="homepage"),
    path('admin/', admin.site.urls),
    path('v1/vote/', question_view.choice_vote, name="question-vote"),
    path('v1/question/list', question_view.question_list, name="question-list"),
    path('v1/question/create', question_view.question_post, name="question-create"),
    path('v1/question/retrieve/<int:pk>', question_view.question_retrieve, name="question-retrieve"),
    path('v1/question/update/<int:pk>', question_view.question_update, name="question-update"),
    path('v1/question/delete/<int:pk>', question_view.question_delete, name="question-delete"),
    path("polls/", polls_view.index_view, name="poll-index"),
    path("polls/<int:pk>/", polls_view.detail_view, name="poll-detail"),
    path("polls/<int:pk>/results/", polls_view.results_view, name="poll-results"),
    path("polls/<int:question_id>/vote/", polls_view.vote, name="poll-vote"),

]


