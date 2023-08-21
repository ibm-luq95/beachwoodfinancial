# -*- coding: utf-8 -*-#
from django.urls import path, include

from special_assignment.views import (
    SpecialAssignmentDetailsView,
    SpecialAssignmentCreateView,
    SpecialAssignmentUpdateView,
    SpecialAssignmentDeleteView,
    SpecialAssignmentListView,
)

app_name = "special_assignment"

urlpatterns = [
    path("", SpecialAssignmentListView.as_view(), name="list"),
    path("create", SpecialAssignmentCreateView.as_view(), name="create"),
    path("<uuid:pk>", SpecialAssignmentDetailsView.as_view(), name="details"),
    path("update/<uuid:pk>", SpecialAssignmentUpdateView.as_view(), name="update"),
    path("delete/<uuid:pk>", SpecialAssignmentDeleteView.as_view(), name="delete"),
    path("api/", include("special_assignment.urls.api"), name="api"),
]
