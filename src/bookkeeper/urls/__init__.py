# -*- coding: utf-8 -*-#
from django.urls import path, include

from bookkeeper.views import (
    BookkeeperListView,
    BookkeeperCreateView,
    BookkeeperDeleteView,
    BookkeeperDetailsView,
    BookkeeperUpdateView,
)

app_name = "management_bookkeeper"

urlpatterns = [
    path("", BookkeeperListView.as_view(), name="list"),
    path("create", BookkeeperCreateView.as_view(), name="create"),
    path("update/<uuid:pk>", BookkeeperUpdateView.as_view(), name="update"),
    path("delete/<uuid:pk>", BookkeeperDeleteView.as_view(), name="delete"),
    path("<uuid:pk>", BookkeeperDetailsView.as_view(), name="details"),
]
