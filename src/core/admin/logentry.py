# -*- coding: utf-8 -*-#
from django.contrib import admin
from django.contrib.admin.models import LogEntry
from import_export.admin import ImportExportModelAdmin


@admin.register(LogEntry)
class LogEntryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        "action_time",
        "user",
        "content_type",
        "change_message",
        "action_flag",
        "object_id",
    )
