# -*- coding: utf-8 -*-#
from django.contrib import admin

from core.admin import BWBaseAdminModelMixin
from reports.models import ClientJobsReportsDBView

from import_export.admin import ImportExportModelAdmin


@admin.register(ClientJobsReportsDBView)
class ClientJobsReportAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [
        "client_id",
        "client_name",
        "job_completed_count",
        "job_archived_count",
        "job_not_started_count",
        "job_draft_count",
        "job_in_progress_count",
        "job_past_due_count",
        "job_not_completed_count",
        "job_year",
        "job_month",
    ]
