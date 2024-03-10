# -*- coding: utf-8 -*-#
from django.contrib import admin

from core.admin import BWBaseAdminModelMixin
from staff_briefcase.models import StaffBriefcase


@admin.register(StaffBriefcase)
class StaffBriefcaseAdmin(BWBaseAdminModelMixin):
    list_display = [
        "pk",
        "user",
        "notes_count",
        "documents_count",
        "created_at",
    ]
    list_filter = ["user"]

    def notes_count(self, obj: StaffBriefcase) -> int:
        return obj.notes.count()

    def documents_count(self, obj: StaffBriefcase) -> int:
        return obj.documents.count()
