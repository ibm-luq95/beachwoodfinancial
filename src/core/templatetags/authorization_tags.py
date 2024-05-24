# -*- coding: utf-8 -*-#
"""
File: authorization_tags.py
Author: Ibrahim Luqman
Date: 5/13/24

Description: Templatetags used for authorization in templates
"""
from typing import List

from django import template
from django.contrib.auth.context_processors import PermWrapper

register = template.Library()


@register.simple_tag
def check_user_permissions(
    perms: PermWrapper, app_name: str, perm_name: str, is_include_app_name: bool = True
) -> bool:
    """
    Check if the user has the specified permission.

    Args:
        perms (PermWrapper): The permission wrapper object.
        app_name (str): The name of the app.
        perm_name (str): The name of the permission.
        is_include_app_name (bool, optional): Whether to include the app name in the permission name. Defaults to True.

    Returns:
        bool: True if the user has the permission, False otherwise.

    """
    plurals_names: List[str] = ["company_services", "jobs"]
    replaced_app_name: str = app_name.replace("_", "")
    if is_include_app_name:
        full_permission_name: str = f"{app_name}.{perm_name}_{replaced_app_name}"
    else:
        full_permission_name: str = f"{app_name}.{perm_name}"
    if app_name in plurals_names:
        full_permission_name = full_permission_name.rstrip("s")
    check_permission: bool = perms.user.has_perm(full_permission_name)
    return check_permission
