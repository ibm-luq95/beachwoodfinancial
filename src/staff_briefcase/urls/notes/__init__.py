# -*- coding: utf-8 -*-#
from django.urls import path, include

from staff_briefcase.views.notes import (
    StaffNotesListView,
    StaffNotesUpdateView,
    StaffNotesCreateView,
    StaffNotesDeleteView,
)

app_name = "briefcase_staff_notes"

urlpatterns = [
    path("api/", include("staff_briefcase.urls.notes.api"), name="staff-notes-api"),
    path("", StaffNotesListView.as_view(), name="list"),
    path("update/<uuid:pk>", StaffNotesUpdateView.as_view(), name="update"),
    path("create", StaffNotesCreateView.as_view(), name="create"),
    path("delete/<uuid:pk>", StaffNotesDeleteView.as_view(), name="delete"),
]

