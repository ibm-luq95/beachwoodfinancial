# -*- coding: utf-8 -*-#
from django.urls import path

from document.views import (
    DocumentUpdateView,
    DocumentCreateView,
    DocumentListView,
    DocumentDeleteView,
)

app_name = "document"

urlpatterns = [
    path("", DocumentListView.as_view(), name="list"),
    path("create", DocumentCreateView.as_view(), name="create"),
    path("update/<uuid:pk>", DocumentUpdateView.as_view(), name="update"),
    path("delete/<uuid:pk>", DocumentDeleteView.as_view(), name="delete"),
]
