from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entrie>", views.entries, name="entrie"),
    path("search/", views.search, name="search"),
    path("/random", views.randompage, name="random"),
    path("newpage/", views.newpage, name="newpage"),
    path("edit/<str:entrie>", views.edit, name="edit"),
]
