# -*- coding: utf-8 -*-#
from django.urls import path, include

from reports.views.new_report import NewReportView

app_name = "reports"

urlpatterns = [
    path("clients/", include("reports.urls.client"), name="clients_reports"),
    path("new", NewReportView.as_view(), name="new_report"),
    # path("create", "", name="create"),
    # path("update/<uuid:pk>", "", name="update"),
    # path("delete/<uuid:pk>", "", name="delete"),
]
