# -*- coding: utf-8 -*-#
from django.urls import path, include

from discussion.views import DiscussionListView

app_name = "discussion"

urlpatterns = [
    path("", DiscussionListView.as_view(), name="list"),
    path("api/", include("discussion.urls.api"), name="apis"),
    # path("create", "", name="create"),
    # path("update/<uuid:pk>", "", name="update"),
    # path("delete/<uuid:pk>", "", name="delete"),
]
