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
