from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("<int:id>", views.test1, name="test1"),
    path("index/", views.index, name="index"),
]