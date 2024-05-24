# -*- coding: utf-8 -*-#
from typing import Optional, List

from django.contrib import admin
from django.db.models import Model, QuerySet
from django.http import HttpRequest


class ReadOnlyInlineMixin(admin.TabularInline):
    """
    Mixin class for readonly inline admin models.

    This mixin class provides readonly functionality for inline admin models.
    It disables change, add, and delete permissions for the inline models.

    Attributes:
        None

    Methods:
        has_change_permission(self, request: HttpRequest, obj: Optional[Model] = None) -> bool:
            Returns False, disabling change permission for the inline models.

        has_add_permission(self, request: HttpRequest, obj: Optional[Model] = None) -> bool:
            Returns False, disabling add permission for the inline models.

        has_delete_permission(self, request: HttpRequest, obj: Optional[Model] = None) -> bool:
            Returns False, disabling delete permission for the inline models.

        get_readonly_fields(self, request: HttpRequest, obj: Optional[Model] = None) -> List[str]:
            Returns a list of all fields, making them readonly.

        get_queryset(self, request: HttpRequest) -> QuerySet:
            Returns the queryset for the inline models.

    """

    def has_change_permission(
        self, request: HttpRequest, obj: Optional[Model] = None
    ) -> bool:
        """
        Returns False, disabling change permission for the inline models.
        """
        return False

    def has_add_permission(
        self, request: HttpRequest, obj: Optional[Model] = None
    ) -> bool:
        """
        Returns False, disabling add permission for the inline models.
        """
        return False

    def has_delete_permission(
        self, request: HttpRequest, obj: Optional[Model] = None
    ) -> bool:
        """
        Returns False, disabling delete permission for the inline models.
        """
        return False

    def get_readonly_fields(
        self, request: HttpRequest, obj: Optional[Model] = None
    ) -> List[str]:
        """
        Returns a list of all fields, making them readonly.
        """
        return list(super().get_fields(request, obj))

    def get_queryset(self, request: HttpRequest) -> QuerySet:
        """
        Returns the queryset for the inline models.
        """
        qs = self.model.original_objects.get_queryset()
        return qs
