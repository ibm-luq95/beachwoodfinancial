# -*- coding: utf-8 -*-#
from django.urls import path, include
from dashboard.views.manager import DashboardViewBW

app_name = "manager"

urlpatterns = [
    path("", DashboardViewBW.as_view(), name="home"),
    path("api/", include("dashboard.urls.api"), name="dashboard-manager-api-urls"),
]
