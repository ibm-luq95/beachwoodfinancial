# -*- coding: utf-8 -*-#
from typing import Any

from django import template

register = template.Library()


@register.simple_tag
def define_var(val: Any) -> Any:
    return val
