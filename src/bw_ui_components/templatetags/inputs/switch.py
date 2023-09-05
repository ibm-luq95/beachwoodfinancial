# -*- coding: utf-8 -*-#
from django import template

from core.utils import get_request_context, debugging_print

register = template.Library()


@register.inclusion_tag("bw_ui_components/inputs/switch.html", takes_context=True)
def bw_switch(context, *args, **kwargs) -> dict:
    context_data = get_request_context(context, kwargs)
    return {**context_data, **kwargs}
