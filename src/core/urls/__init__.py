# -*- coding: utf-8 -*-#
from django.urls import path, include

app_name = "core"

urlpatterns = [
    path("api/", include("core.urls.api"), name="core-api-urls"),
]
