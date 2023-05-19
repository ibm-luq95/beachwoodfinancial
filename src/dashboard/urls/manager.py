# -*- coding: utf-8 -*-#
from django.urls import path, include
from dashboard.views.manager import DashboardView

app_name = "manager"

urlpatterns = [
    path("", DashboardView.as_view(), name="home"),
]
