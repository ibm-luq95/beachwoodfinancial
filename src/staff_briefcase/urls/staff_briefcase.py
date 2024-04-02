# -*- coding: utf-8 -*-#
from django.urls import path, include

from staff_briefcase.views import (
    StaffBriefcaseListView,
    StaffBriefcaseDetailView,
    StaffBriefcaseCreateView,
)

app_name = "briefcase"

urlpatterns = [
    path("", StaffBriefcaseListView.as_view(), name="list"),
    path("<uuid:pk>", StaffBriefcaseDetailView.as_view(), name="details"),
    path("create", StaffBriefcaseCreateView.as_view(), name="create"),
    path("notes/", include("staff_briefcase.urls.notes"), name="staff-notes-root"),
    path(
        "documents/",
        include("staff_briefcase.urls.documents"),
        name="staff-documents-root",
    ),
    path(
        "accounts/",
        include("staff_briefcase.urls.accounts"),
        name="staff-accounts-root",
    ),
    # path("update/<uuid:pk>", "", name="update"),
    # path("delete/<uuid:pk>", "", name="delete"),
]
