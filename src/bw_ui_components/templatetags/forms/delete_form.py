# -*- coding: utf-8 -*-#
from django import template
from django.urls import reverse_lazy

from core.utils import get_request_context, debugging_print

register = template.Library()


@register.inclusion_tag("bw_ui_components/forms/delete_form.html", takes_context=True)
def bw_delete_form(context, *args, **kwargs) -> dict:
    context_data = get_request_context(context, kwargs)
    cancel_url = kwargs.get("cancel_url")
    cancel_url = reverse_lazy(cancel_url)
    kwargs.update({"cancel_url": cancel_url})
    # debugging_print(kwargs)
    return {**context_data, **kwargs}
