# -*- coding: utf-8 -*-#
from django.urls import path, include

from client.views import (
    ClientListView,
    ClientCreateView,
    ClientUpdateView,
    ClientDeleteView,
    ClientDetailsView,
    ClientReportView,
)

app_name = "client"

urlpatterns = [
    path("", ClientListView.as_view(), name="list"),
    path("create", ClientCreateView.as_view(), name="create"),
    path("update/<uuid:pk>", ClientUpdateView.as_view(), name="update"),
    path("delete/<uuid:pk>", ClientDeleteView.as_view(), name="delete"),
    path("<uuid:pk>", ClientDetailsView.as_view(), name="details"),
    path("api/", include("client.urls.api"), name="api"),
    path("jobs-report", ClientReportView.as_view(), name="jobs_report"),
]
