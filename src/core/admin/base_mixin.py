from django.contrib import admin
from import_export.admin import ImportExportModelAdmin


class BaseAdminModelMixin(ImportExportModelAdmin, admin.ModelAdmin):
    list_filter = ("created_at", "updated_at")
    exclude = ("metadata", "is_deleted", "deleted_at")
