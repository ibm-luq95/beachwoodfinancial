# -*- coding: utf-8 -*-#
from django import template
from django.urls import reverse_lazy

from core.constants.css_classes import (
    BW_PRELINE_INPUT_SUCCESS_STATE,
    BW_PRELINE_INPUT_DANGER_STATE,
)
from core.utils import get_request_context, debugging_print

register = template.Library()


@register.inclusion_tag("bw_ui_components/table_list/filter_form.html", takes_context=True)
def bw_tl_filter_form(context, *args, **kwargs) -> dict:
    context_data = get_request_context(context, kwargs)
    filter_cancel_url = kwargs.get("filter_cancel_url")
    try:
        filter_cancel_url = reverse_lazy(filter_cancel_url)
    except:
        pass
    kwargs.update({"filter_cancel_url": filter_cancel_url})
    return {**context_data, **kwargs}
