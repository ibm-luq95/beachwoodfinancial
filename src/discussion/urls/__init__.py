# -*- coding: utf-8 -*-#
from django.urls import path, include

app_name = "discussion"

urlpatterns = [
    path("api/", include("discussion.urls.api"), name="apis"),
    # path("create", "", name="create"),
    # path("update/<uuid:pk>", "", name="update"),
    # path("delete/<uuid:pk>", "", name="delete"),
]
