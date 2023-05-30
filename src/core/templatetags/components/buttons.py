# -*- coding: utf-8 -*-#
from django import template
from django.template.context import ContextDict

from core.utils import debugging_print

register = template.Library()


#
@register.inclusion_tag("bw_components/components/button.html", takes_context=True)
# @register.inclusion_tag("bw_components/components/button.html")
def bw_button(context, *args, **kwargs) -> dict:
    # def bw_button(*args, **kwargs) -> dict:
    full_dict = kwargs
    # debugging_print(locals())
    # debugging_print(context)
    # debugging_print(type(context))
    # debugging_print(dir(context))
    for co in context:
        debugging_print(type(co))
        debugging_print(co)
        if isinstance(co, dict):
            full_dict.update(co)
        print("##############################################")
    debugging_print(context.get("BW_BASE_INPUT_CSS_CLASSES"))
    return full_dict
