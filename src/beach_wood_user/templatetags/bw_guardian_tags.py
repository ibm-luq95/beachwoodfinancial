# -*- coding: utf-8 -*-#
from django import template
from guardian.shortcuts import get_objects_for_user

register = template.Library()


@register.filter(name="bw_has_perm")
def bw_has_perm(user, permission):
    return get_objects_for_user(user, permission).exists()
