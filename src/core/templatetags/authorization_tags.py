# -*- coding: utf-8 -*-#

from django import template
from django.contrib.auth.context_processors import PermWrapper

register = template.Library()


@register.simple_tag
def check_user_permissions(
    perms: PermWrapper, app_name: str, perm_name: str, is_include_app_name=True
) -> bool:
    plurals_names = ["company_services", "jobs"]
    replaced_app_name = app_name.replace("_", "")
    if is_include_app_name is True:
        full_permission_name = f"{app_name}.{perm_name}_{replaced_app_name}"
    else:
        full_permission_name = f"{app_name}.{perm_name}"
    if app_name in plurals_names:
        full_permission_name = full_permission_name.rstrip("s")
    check_permission = perms.user.has_perm(full_permission_name)
    # debugging_print(locals())
    return check_permission
