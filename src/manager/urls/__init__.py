# -*- coding: utf-8 -*-#
from django.urls import path, include
from manager.views import (
    ManagerDeleteView,
    ManagerUpdateView,
    ManagerCreateView,
    ManagerListView,
)

app_name = "managers"

urlpatterns = [
    path("", ManagerListView.as_view(), name="list"),
    path("create", ManagerCreateView.as_view(), name="create"),
    path("update/<uuid:pk>", ManagerUpdateView.as_view(), name="update"),
    path("delete/<uuid:pk>", ManagerDeleteView.as_view(), name="delete"),
    # path("<uuid:pk>", ManagerDetailsView.as_view(), name="details"),
]
