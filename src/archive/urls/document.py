# -*- coding: utf-8 -*-#
from django.urls import path

from archive.views.document import DocumentArchiveListView

app_name = "documents"

urlpatterns = [
    path("archive", DocumentArchiveListView.as_view(), name="list"),
]
