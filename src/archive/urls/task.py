# -*- coding: utf-8 -*-#
from django.urls import path, include

from archive.views.task import TaskArchiveListView

app_name = "tasks"

urlpatterns = [
    path("archive", TaskArchiveListView.as_view(), name="list"),
]
