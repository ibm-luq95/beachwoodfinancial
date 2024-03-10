# -*- coding: utf-8 -*-#
from django.contrib import admin

from client.models import ClientProxy
from core.admin import BWBaseAdminModelMixin
from core.admin.tabularinline_readonly_mixin import ReadOnlyInlineMixin
from job.models import JobProxy


class JobsInline(ReadOnlyInlineMixin):
    model = JobProxy
    can_delete = False
    extra = 0
    # readonly_fields = ["title", "managed_by", "start_date", "due_date", "status"]
    fields = [
        "title",
        "managed_by",
        "period_year",
        "period_month",
        "start_date",
        "due_date",
        "status",
    ]
    save_as_continue = False


@admin.register(ClientProxy)
class ClientAdmin(BWBaseAdminModelMixin):
    list_display = ("name", "email", "industry", "status", "created_at")
    list_filter = ["status", "industry"] + BWBaseAdminModelMixin.list_filter
    search_fields = ("email",)
    inlines = [JobsInline]
