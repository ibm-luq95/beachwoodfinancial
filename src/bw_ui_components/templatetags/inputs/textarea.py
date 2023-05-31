# -*- coding: utf-8 -*-#
from django import template

register = template.Library()


@register.inclusion_tag("bw_ui_components/inputs/button.html", takes_context=True)
def bw_textarea(context, *args, **kwargs) -> dict:
    return {}
