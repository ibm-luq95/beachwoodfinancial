# -*- coding: utf-8 -*-#
from django.urls import path, include
from manager.views import (
    ManagerDeleteView,
    ManagerUpdateView,
    ManagerCreateView,
    ManagerListView,
)
from manager.views.schedule_jobs import JobScheduleListView

app_name = "managers"

urlpatterns = [
    path("", ManagerListView.as_view(), name="list"),
    path("create", ManagerCreateView.as_view(), name="create"),
    path("update/<uuid:pk>", ManagerUpdateView.as_view(), name="update"),
    path("delete/<uuid:pk>", ManagerDeleteView.as_view(), name="delete"),
    path("schedule", JobScheduleListView.as_view(), name="schedule_jobs_list"),
    # path("<uuid:pk>", ManagerDetailsView.as_view(), name="details"),
]
