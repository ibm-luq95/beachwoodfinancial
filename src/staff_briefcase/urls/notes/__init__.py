# -*- coding: utf-8 -*-#
from django.urls import path, include

app_name = "briefcase_staff_notes"

urlpatterns = [
    path("api/", include("staff_briefcase.urls.notes.api"), name="staff-notes-api"),
]
