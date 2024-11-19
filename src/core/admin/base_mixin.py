from typing import Tuple, List

from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest
from django.utils.translation import gettext as _
from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import DateRangeFilterBuilder


class BWBaseAdminModelMixin(ImportExportModelAdmin, admin.ModelAdmin):
    """
    Mixin class for admin models in Beachwood Wood Financial.

    This mixin class provides common functionality for admin models in Beachwood Wood Financial.
    It includes import/export functionality and customizes the list filter and excluded fields.

    Attributes:
        import_error_display (Tuple[str, str, str]): Specifies the fields to display for import error messages.
        list_filter (List[Tuple[str, DateRangeFilterBuilder]]): Specifies the list filters for the admin model.
        exclude (Tuple[str, str, str]): Specifies the fields to exclude from the admin model.

    Methods:
        get_queryset(self, request: HttpRequest) -> QuerySet: Returns the queryset for the admin model.

    """

    import_error_display: Tuple[str, str, str] = ("message", "row", "traceback")
    list_filter: List[Tuple[str, DateRangeFilterBuilder]] = [
        ("created_at", DateRangeFilterBuilder(title=_("Created at"))),
        ("updated_at", DateRangeFilterBuilder(title=_("Updated at"))),
    ]
    exclude: Tuple[str, str, str] = ("metadata", "is_deleted", "deleted_at")

    def get_queryset(self, request: HttpRequest) -> QuerySet:
        """
        Returns the queryset for the admin model.

        Args:
            request (HttpRequest): The request object.

        Returns:
            QuerySet: The queryset for the admin model.

        """
        qs = self.model.original_objects.get_queryset()
        return qs
