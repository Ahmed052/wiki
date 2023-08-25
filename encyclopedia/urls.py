from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>/", views.entry_page, name="Entry_page"),
    path("search", views.search, name="search"),
    path("newpage", views.new_page, name="new_page"),
    path("random", views.random_page, name="random"),
    path("edit", views.edit, name="edit" ),
    path("save", views.save, name="save")

    
]
