# -*- coding: utf-8 -*-#
from django import template

from core.utils import get_request_context

register = template.Library()


@register.inclusion_tag("bw_ui_components/inputs/_method_input.html", takes_context=True)
def bw_hidden_method_input(context, *args, **kwargs) -> dict:
    context_data = get_request_context(context, kwargs)
    return {**context_data, **kwargs}
