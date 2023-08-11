# -*- coding: utf-8 -*-#
from django import template
from django.urls import reverse_lazy

from core.utils import get_request_context, debugging_print

register = template.Library()


@register.inclusion_tag("bw_ui_components/elements/js_modal.html", takes_context=True)
def bw_js_modal(context, *args, **kwargs) -> dict:
    context_data = get_request_context(context, kwargs)
    url = ""
    action_url = kwargs.get("action_url", None)
    action_url_pk = kwargs.get("action_url_pk", None)
    extra_hidden_inputs = kwargs.get("extra_hidden_inputs", None)
    debugging_print(f"extra_hidden_inputs -> {extra_hidden_inputs}")
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

    return {**context_data, **kwargs}
