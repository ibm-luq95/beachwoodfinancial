# -*- coding: utf-8 -*-#
from django.contrib import admin


class ReadOnlyInlineMixin(admin.TabularInline):
    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_readonly_fields(self, request, obj=None):
        return list(super().get_fields(request, obj))

    def get_queryset(self, request):
        # queryset = super().get_queryset(request)
        # queryset = queryset.prefetch_related('car').all()
        qs = self.model.original_objects.get_queryset()
        return qs
