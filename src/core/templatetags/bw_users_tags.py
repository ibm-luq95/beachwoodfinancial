# -*- coding: utf-8 -*-#
from typing import Any

from django import template

from beach_wood_user.models import BWUser

register = template.Library()


@register.simple_tag
def bw_get_staff_member_pk(user: BWUser, return_full_object=False) -> Any:
    if return_full_object is True:
        return getattr(user, user.user_type)
    pk = getattr(user, user.user_type).pk
    return pk
