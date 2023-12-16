# -*- coding: utf-8 -*-#
from django.urls import path

from archive.views.client import ClientArchiveListView

app_name = "clients"

urlpatterns = [
    path("archive", ClientArchiveListView.as_view(), name="list"),
]
