# -*- coding: utf-8 -*-#
from django import template

register = template.Library()


@register.filter(name="get_var_type")
def get_var_type(var) -> str:
    return type(var)
