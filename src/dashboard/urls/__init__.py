# -*- coding: utf-8 -*-#
from django.urls import path, include

app_name = "dashboard"

urlpatterns = [
    path("manager/", include("dashboard.urls.manager"), name="dashboard-manager-urls"),
    path(
        "bookkeeper/",
        include("dashboard.urls.bookkeeper"),
        name="dashboard-bookkeeper-urls",
    ),
    path(
        "client-category/",
        include("dashboard.urls.client_category"),
        name="client-category",
    ),
]
