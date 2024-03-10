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
    # path("update/<uuid:pk>", "", name="update"),
    # path("delete/<uuid:pk>", "", name="delete"),
]
