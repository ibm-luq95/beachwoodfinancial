# -*- coding: utf-8 -*-#
from django.urls import path, include

from archive.views.job import JobArchiveListView

app_name = "jobs"

urlpatterns = [
    path("archive", JobArchiveListView.as_view(), name="list"),
]
