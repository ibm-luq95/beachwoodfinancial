# -*- coding: utf-8 -*-#
from django.urls import path, include
from dashboard.views.manager import ManagementDashboardApiView

app_name = "management_api"

urlpatterns = [
    path(
        "management-dashboard-api",
        ManagementDashboardApiView.as_view(),
        name="management-dashboard-api",
    )
]
