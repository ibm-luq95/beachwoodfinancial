# -*- coding: utf-8 -*-#
from django.urls import path, include
from discussion.views.api import CreateDiscussionApiView

app_name = "api"

urlpatterns = [path("create", CreateDiscussionApiView.as_view(), name="create")]
