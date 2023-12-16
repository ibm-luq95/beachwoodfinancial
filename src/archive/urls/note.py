# -*- coding: utf-8 -*-#
from django.urls import path

from archive.views.note import NoteArchiveListView

app_name = "notes"

urlpatterns = [
    path("archive", NoteArchiveListView.as_view(), name="list"),
]
