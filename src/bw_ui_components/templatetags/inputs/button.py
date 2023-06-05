# -*- coding: utf-8 -*-#
from django import template

from core.constants.css_classes import (
    BW_PRELINE_INPUT_SUCCESS_STATE,
    BW_PRELINE_INPUT_DANGER_STATE,
)
from core.utils import get_request_context, debugging_print

register = template.Library()


@register.inclusion_tag("bw_ui_components/inputs/button.html", takes_context=True)
def bw_button(context, *args, **kwargs) -> dict:
    context_data = get_request_context(context, kwargs)
    data_aria_attributes = ""
    btn_variant = kwargs.get("btn_variant").upper()
    is_soft_color = bool(kwargs.get("is_soft_color"))
    is_disabled = "disabled" if kwargs.get("is_disabled") else ""
    btn_size = kwargs.get("btn_size", "DEFAULT").upper()

    btn_css_classes = context_data.get("SOLID_COLORS_CSS_CLASSES").get(btn_variant)
    if is_soft_color is True:
        btn_css_classes = context_data.get("SOFT_COLORS_CSS_CLASSES").get(btn_variant)
    btn_css_classes += context_data.get("BW_DEFAULT_BUTTONS_CSS_CLASSES").get(btn_size)
    for key, value in kwargs.items():
        if key.startswith("data_") or key.startswith("aria_"):
            new_data_name = key.replace("_", "-")
            data_aria_attributes += f"{new_data_name}={value} "
    data_aria_attributes = data_aria_attributes.strip()
    if is_disabled:
        btn_css_classes += " cursor-not-allowed"
    kwargs.update({"btn_css_classes": btn_css_classes})
    # debugging_print(kwargs)

    return {
        **context_data,
        **kwargs,
        "is_disabled": is_disabled,
    }
