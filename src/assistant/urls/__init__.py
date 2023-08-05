# -*- coding: utf-8 -*-#
from django.urls import path

from assistant.views import (
    AssistantCreateView,
    AssistantListView,
    AssistantUpdateView,
    AssistantDetailsView,
    AssistantDeleteView,
)

app_name = "management_assistant"

urlpatterns = [
    path("", AssistantListView.as_view(), name="list"),
    path("create", AssistantCreateView.as_view(), name="create"),
    path("update/<uuid:pk>", AssistantUpdateView.as_view(), name="update"),
    path("delete/<uuid:pk>", AssistantDeleteView.as_view(), name="delete"),
    path("<uuid:pk>", AssistantDetailsView.as_view(), name="details"),
]
