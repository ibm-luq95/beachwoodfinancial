# -*- coding: utf-8 -*-#
from django.contrib import admin

from core.admin import BWBaseAdminModelMixin
from staff_briefcase.models import StaffNotes, StaffBriefcase


class StaffBriefcaseInline(admin.TabularInline):
    model = StaffBriefcase.notes.through
    extra = 1
    max_num = 1
    show_change_link = False


@admin.register(StaffNotes)
class StaffNotesAdmin(BWBaseAdminModelMixin):
    inlines = [StaffBriefcaseInline]
    list_display = ["title", "note_body", "get_briefcase", "created_at"]
    list_filter = ["briefcase"]


__all__ = [StaffNotesAdmin]
