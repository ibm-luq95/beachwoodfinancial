# -*- coding: utf-8 -*-#
import json
import ast
from django import template
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe

from core.utils import get_request_context, debugging_print

register = template.Library()


@register.inclusion_tag("bw_ui_components/elements/js_modal.html", takes_context=True)
def bw_js_modal(context, *args, **kwargs) -> dict:
    context_data = get_request_context(context, kwargs)
    url = ""
    action_url = kwargs.get("action_url", None)
    action_url_pk = kwargs.get("action_url_pk", None)
    extra_hidden_inputs = kwargs.get("extra_hidden_inputs", None)
    extra_hidden_inputs_markup_list = []
    if extra_hidden_inputs is not None:
        # extra_hidden_inputs = str(extra_hidden_inputs)
        extra_hidden_inputs = ast.literal_eval(extra_hidden_inputs)
        for name, value in extra_hidden_inputs.items():
            tmp_markup = f"<input type='hidden' name='{name}' value='{value}' />"
            extra_hidden_inputs_markup_list.append(mark_safe(tmp_markup))
    # debugging_print(extra_hidden_inputs_markup_list)
    modal_size = kwargs.get("modal_size", "sm")
    modal_size_css_classes = ""
    match modal_size:
        case "sm" | "small" | "default" | "s" | "d":
            modal_size_css_classes = "sm:max-w-lg sm:w-full sm:mx-auto"
        case "md" | "medium" | "m":
            modal_size_css_classes = "md:max-w-2xl md:w-full md:mx-auto"
        case "lg" | "large" | "l":
            modal_size_css_classes = "lg:max-w-4xl lg:w-full lg:mx-auto"

    if action_url is not None:
        url = reverse_lazy(action_url)
        if action_url_pk is not None:
            url = reverse_lazy(action_url, kwargs={"pk": action_url_pk})
        context_data.update({"form_action_url": url})
    # debugging_print(url)
    context_data.update({"modal_size_css_classes": modal_size_css_classes})
    context_data.update(
        {"extra_hidden_inputs_markup_list": extra_hidden_inputs_markup_list}
    )

    return {**context_data, **kwargs}
