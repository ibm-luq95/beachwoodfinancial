# -*- coding: utf-8 -*-#
from django.contrib import admin

from core.admin import BWBaseAdminModelMixin
from special_assignment.models import SpecialAssignmentProxy


@admin.register(SpecialAssignmentProxy)
class SpecialAssignmentAdmin(BWBaseAdminModelMixin):
    list_filter = ("status", "client", "job", "updated_by_cron")
    list_display = (
        "title",
        "client",
        "job",
        "manager",
        "assigned_by",
        "status",
        "is_seen",
        "attachment",
        "updated_by_cron",
        "created_at",
    )
