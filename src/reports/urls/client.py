# -*- coding: utf-8 -*-#
from django.urls import path, include

from reports.views.client import JobsReportView

app_name = "clients_reports"

urlpatterns = [path("jobs-report", JobsReportView.as_view(), name="job_reports_list")]
