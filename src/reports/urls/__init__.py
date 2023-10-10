# -*- coding: utf-8 -*-#
from django.urls import path, include

app_name = "reports"

urlpatterns = [
    path("clients/", include("reports.urls.client"), name="clients_reports"),
    # path("create", "", name="create"),
    # path("update/<uuid:pk>", "", name="update"),
    # path("delete/<uuid:pk>", "", name="delete"),
]
