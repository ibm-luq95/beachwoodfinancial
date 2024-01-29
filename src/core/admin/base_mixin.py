from django.contrib import admin
from django.utils.translation import gettext as _

from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import DateRangeFilterBuilder


class BWBaseAdminModelMixin(ImportExportModelAdmin, admin.ModelAdmin):
    # list_filter = ("created_at", "updated_at")
    list_filter = [
        ("created_at", DateRangeFilterBuilder(title=_("Created at"))),
        ("updated_at", DateRangeFilterBuilder(title=_("Updated at"))),
    ]
    exclude = ("metadata", "is_deleted", "deleted_at")

    def get_queryset(self, request):
        # queryset = super().get_queryset(request)
        # queryset = queryset.prefetch_related('car').all()
        qs = self.model.original_objects.get_queryset()
        return qs
