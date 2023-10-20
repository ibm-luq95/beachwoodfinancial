# -*- coding: utf-8 -*-#
from django.contrib import admin

from job.models import JobProxy
from core.admin import BWBaseAdminModelMixin


@admin.register(JobProxy)
class JobAdmin(BWBaseAdminModelMixin):
    list_display = (
        "title",
        "client",
        "status",
        "start_date",
        "due_date",
        "job_type",
        "managed_by",
        "created_at",
    )
