from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import DateRangeFilterBuilder


class BWBaseAdminModelMixin(ImportExportModelAdmin, admin.ModelAdmin):
    # list_filter = ("created_at", "updated_at")
    list_filter = [
        ("created_at", DateRangeFilterBuilder(title="Created at")),
        ("updated_at", DateRangeFilterBuilder(title="Updated at")),
    ]
    exclude = ("metadata", "is_deleted", "deleted_at")
