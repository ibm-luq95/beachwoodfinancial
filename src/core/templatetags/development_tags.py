# -*- coding: utf-8 -*-#
from django import template

from core.utils import debugging_print

register = template.Library()


@register.filter(name="get_var_type")
def get_var_type(var) -> str:
    return type(var)


@register.filter(name="dir_var")
def dir_var(var):
    debugging_print(dir(var))
