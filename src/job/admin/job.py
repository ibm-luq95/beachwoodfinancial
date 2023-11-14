# -*- coding: utf-8 -*-#
from django.contrib import admin

from job.models import JobProxy
from core.admin import BWBaseAdminModelMixin


@admin.register(JobProxy)
class JobAdmin(BWBaseAdminModelMixin):
    search_fields = ("title", "client", "status", "managed_by", "state", "job_type")
    list_display = (
        "title",
        "client",
        "job_type",
        "status",
        "start_date",
        "due_date",
        "state",
        "managed_by",
        "updated_by_cron",
        "created_at",
    )
