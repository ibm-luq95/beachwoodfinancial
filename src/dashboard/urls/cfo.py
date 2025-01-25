# -*- coding: utf-8 -*-#
from django.urls import path, include
from dashboard.views.cfo.dashboard import DashboardView

app_name = "cfo"

urlpatterns = [
    path("", DashboardView.as_view(), name="home"),
]
