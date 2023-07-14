# -*- coding: utf-8 -*-#
from django import template

from core.utils import get_request_context, debugging_print

register = template.Library()


@register.inclusion_tag("bw_ui_components/global/badge.html", takes_context=True)
def bw_badge(context, *args, **kwargs) -> dict:
    context_data = get_request_context(context, kwargs)
    size = kwargs.get("size", None)
    font_size = "text-xs"
    badge_size = "py-1.5 px-3"
    if size is not None:
        match size:
            case "lg":
                badge_size = "py-2 px-4"
                font_size = "text-lg"
            case "md":
                badge_size = "py-2 px-3"
                font_size = "text-sm"
            case "default":
                badge_size = "py-1.5 px-3"
                # font_size = "text-xs"
                font_size = "text-sm"
            case "sm":
                badge_size = "py-1 px-2"
                font_size = "text-xs"
    else:
        badge_size = "py-1.5 px-3"
    kwargs.update({"badge_size": badge_size})
    kwargs.update({"font_size": font_size})
    return {**context_data, **kwargs}
