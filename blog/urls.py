from django.urls import path

from blog import views

app_name = "blog"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<str:slug>/", views.DetailView.as_view(), name="detail"),
]
