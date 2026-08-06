# -*- coding: utf-8 -*-#
from __future__ import annotations

from typing import Tuple

from django.http import HttpRequest
from rest_framework import permissions
from rest_framework.views import APIView

from core.choices import BeachWoodUserTypeEnum


class ManagerApiPermission(permissions.BasePermission):
    """
    Permission class restricting API access to managers and assistants only.

    Attributes:
        edit_methods (Tuple[str]): The HTTP methods for which edit permissions are required.

    """

    edit_methods: Tuple[str] = ("PUT", "PATCH")

    def has_permission(self, request: HttpRequest, view: APIView) -> bool:
        if not request.user or not request.user.is_authenticated:
            return False
        if request.user.is_superuser or request.user.is_staff:
            return True
        if request.user.user_type in (
            BeachWoodUserTypeEnum.MANAGER,
            BeachWoodUserTypeEnum.ASSISTANT,
            BeachWoodUserTypeEnum.CFO,
        ):
            return True
        return False

