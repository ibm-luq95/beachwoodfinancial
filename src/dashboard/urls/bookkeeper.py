# -*- coding: utf-8 -*-#
from django.urls import path, include
from dashboard.views.bookkeeper import DashboardView

app_name = "bookkeeper"

urlpatterns = [
    path("", DashboardView.as_view(), name="home"),
]
