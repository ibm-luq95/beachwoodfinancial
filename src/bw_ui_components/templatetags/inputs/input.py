# -*- coding: utf-8 -*-#
from django import template

from core.constants.css_classes import (
    BW_PRELINE_INPUT_SUCCESS_STATE,
    BW_PRELINE_INPUT_DANGER_STATE,
)
from core.utils import get_request_context, debugging_print

register = template.Library()


@register.inclusion_tag("bw_ui_components/inputs/input.html", takes_context=True)
def bw_input(context, *args, **kwargs) -> dict:
    context_data = get_request_context(context, kwargs)
    input_state = kwargs.get("input_state", None)
    input_state_css_classes = ""
    if input_state is not None:
        match input_state:
            case "success":
                input_state_css_classes = BW_PRELINE_INPUT_SUCCESS_STATE
            case "error":
                input_state_css_classes = BW_PRELINE_INPUT_DANGER_STATE
    kwargs.update({"input_state_css_classes": input_state_css_classes})
    # debugging_print(kwargs)
    return {**context_data, **kwargs}
