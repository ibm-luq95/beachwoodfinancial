# -*- coding: utf-8 -*-#
from typing import Tuple

from django.http import HttpRequest
from rest_framework import permissions
from rest_framework.views import APIView


class ManagerApiPermission(permissions.BasePermission):
    """
    Permission class for API actions related to managers.

    This class provides permission handling for API actions specific to managers.
    It defines permission checks for different HTTP methods.

    Attributes:
        edit_methods (Tuple[str]): The HTTP methods for which edit permissions are required.

    Methods:
        has_permission(self, request: HttpRequest, view: APIView) -> bool:
            Checks if the requesting user has the required permission for the API action.

    """

    edit_methods: Tuple[str] = ("PUT", "PATCH")

    def has_permission(self, request: HttpRequest, view: APIView) -> bool:
        """
        Checks if the requesting user has the required permission for the API action.

        Args:
            request (HttpRequest): The request object.
            view (APIView): The view object.

        Returns:
            bool: True if the user has the required permission, False otherwise.

        """
        if request.user.user_type in ["manager", "assistant"]:
            return True
        if request.method in self.edit_methods:
            return request.user.is_staff
        return True
