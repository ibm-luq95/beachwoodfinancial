# -*- coding: utf-8 -*-#
from django.urls import path

from core.views.api import FetchUrlApiView

app_name = "api"

urlpatterns = [
    path("fetch_url", FetchUrlApiView.as_view(), name="fetch-url"),
]
