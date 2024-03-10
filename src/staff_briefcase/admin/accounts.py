# -*- coding: utf-8 -*-#
from django.contrib import admin

from core.admin import BWBaseAdminModelMixin
from staff_briefcase.models import StaffBriefcase, StaffAccounts


class StaffBriefcaseInline(admin.TabularInline):
    model = StaffBriefcase.accounts.through
    extra = 1
    max_num = 1
    show_change_link = False


@admin.register(StaffAccounts)
class StaffAccountsAdmin(BWBaseAdminModelMixin):
    inlines = [StaffBriefcaseInline]
    # list_display = ["title", "note_body", "get_briefcase", "created_at"]
    # list_filter = ["briefcase"]


__all__ = [StaffAccountsAdmin]
