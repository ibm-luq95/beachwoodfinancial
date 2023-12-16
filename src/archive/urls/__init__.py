# -*- coding: utf-8 -*-#
from django.urls import path, include

app_name = "archive"

urlpatterns = [
    path("jobs/", include("archive.urls.job"), name="jobs"),
    path("clients/", include("archive.urls.client"), name="clients"),
    path("tasks/", include("archive.urls.task"), name="tasks"),
    path("assignments/", include("archive.urls.special_assignment"), name="assignments"),
    path("notes/", include("archive.urls.note"), name="notes"),
    path("documents/", include("archive.urls.document"), name="documents"),
]
