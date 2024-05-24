# -*- coding: utf-8 -*-#
from typing import Dict

from django.http import HttpRequest
from django.utils.translation import gettext as _
from django.views import View
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.permissions import BasePermission


class BaseApiPermissionMixin(BasePermission):
    """
    Mixin class for API permissions based on user permissions.

    This mixin class provides permission handling for API actions based on user permissions.
    It defines a message for unauthorized actions and a permission mapping for different HTTP methods.

    Attributes:
        message (str): The default message for unauthorized actions.
        permission_map (Dict[str, str]): Mapping of HTTP methods to permission strings.

    Methods:
        _get_permission(self, method: str, perm_slug: str) -> str:
            Extracts the permission string based on the HTTP method and permission slug.

        has_permission(self, request: HttpRequest, view: View) -> bool:
            Checks if the requesting user has the required permission for the API action.

    """

    message: str = _("You do not have permission to perform action")
    permission_map: Dict[str, str] = {
        "GET": "{app_label}.view_{model_name}",
        "POST": "{app_label}.add_{model_name}",
        "PUT": "{app_label}.change_{model_name}",
        "PATCH": "{app_label}.change_{model_name}",
        "DELETE": "{app_label}.delete_{model_name}",
    }

    def _get_permission(self, method: str, perm_slug: str) -> str:
        """
        Extracts the permission string based on the HTTP method and permission slug.
        """
        app, model = perm_slug.split(".")
        if method not in self.permission_map:
            raise MethodNotAllowed(method)
        perm: str = self.permission_map.get(method).format(app_label=app, model_name=model)
        return perm

    def has_permission(self, request: HttpRequest, view: View) -> bool:
        """
        Checks if the requesting user has the required permission for the API action.
        """
        perm: str = self._get_permission(method=request.method, perm_slug=view.perm_slug)

        if request.user.has_perm(perm):
            return True
        return False
