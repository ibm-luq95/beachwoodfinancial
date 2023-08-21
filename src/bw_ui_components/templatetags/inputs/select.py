# -*- coding: utf-8 -*-#
import json
from django import template
from django.forms import Select

from core.utils import get_request_context, debugging_print

register = template.Library()


@register.inclusion_tag("bw_ui_components/inputs/select.html", takes_context=True)
def bw_select(context, *args, **kwargs) -> dict:
    # Syntax: {% bw_select options='{"one": "One", "tow": "tow", "three": "three"}' %}
    context_data = get_request_context(context, kwargs)
    options = kwargs.get("options")
    field = kwargs.get("input")
    try:
        if options:
            options = json.loads(options)
            kwargs.update({"options": options})

        # debugging_print(options)
    except json.JSONDecodeError as jerror:
        raise ValueError("Input data is not a valid JSON object: {}".format(str(jerror)))
    return {**context_data, **kwargs}
