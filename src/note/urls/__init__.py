# -*- coding: utf-8 -*-#
from django.urls import path, include

from note.views import NoteListView, NoteUpdateView, NoteDeleteView, NoteCreateView

app_name = "note"

urlpatterns = [
    path("", NoteListView.as_view(), name="list"),
    path("create", NoteCreateView.as_view(), name="create"),
    path("update/<uuid:pk>", NoteUpdateView.as_view(), name="update"),
    path("delete/<uuid:pk>", NoteDeleteView.as_view(), name="delete"),
    path("api/", include("note.urls.api"), name="api"),
]
