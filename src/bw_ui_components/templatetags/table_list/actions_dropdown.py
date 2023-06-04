# -*- coding: utf-8 -*-#
from django import template
from django.urls import reverse_lazy

from core.constants.css_classes import (
    BW_PRELINE_INPUT_SUCCESS_STATE,
    BW_PRELINE_INPUT_DANGER_STATE,
)
from core.utils import get_request_context, debugging_print

register = template.Library()


@register.inclusion_tag(
    "bw_ui_components/table_list/actions_dropdown.html", takes_context=True
)
def bw_actions_dropdown(context, *args, **kwargs) -> dict:
    context_data = get_request_context(context, kwargs)
    actions_items = kwargs.get("actions_items")
    actions_base_url = kwargs.get("actions_base_url")
    actions_app_name = kwargs.get("actions_app_name")
    object_var = kwargs.get("object")
    all_actions_urls_dict = dict()
    try:
        if "update" in actions_items:
            all_actions_urls_dict.update(
                {
                    "update": reverse_lazy(
                        f"{actions_base_url}:update", kwargs={"pk": object_var.pk}
                    )
                }
            )
        if "delete" in actions_items:
            all_actions_urls_dict.update(
                {
                    "delete": reverse_lazy(
                        f"{actions_base_url}:delete", kwargs={"pk": object_var.pk}
                    )
                }
            )
    except:
        pass
    kwargs.update({"action_urls": all_actions_urls_dict})
    return {**context_data, **kwargs}
