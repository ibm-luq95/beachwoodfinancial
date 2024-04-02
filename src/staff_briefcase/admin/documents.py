# -*- coding: utf-8 -*-#
from django.contrib import admin

from core.admin import BWBaseAdminModelMixin
from staff_briefcase.models import StaffDocuments, StaffBriefcase


class StaffBriefcaseInline(admin.TabularInline):
    model = StaffBriefcase.documents.through
    extra = 1
    max_num = 1
    show_change_link = False
    can_delete = False


@admin.register(StaffDocuments)
class StaffDocumentsAdmin(BWBaseAdminModelMixin):
    inlines = [StaffBriefcaseInline]
    list_display = ["title", "document_file", "get_briefcase", "created_at"]
    list_filter = ["briefcase"]
    # list_select_related = ["get_briefcase"]
    # preserve_filters = True
    # show_facets = admin.ShowFacets.ALWAYS


__all__ = [StaffDocumentsAdmin]
