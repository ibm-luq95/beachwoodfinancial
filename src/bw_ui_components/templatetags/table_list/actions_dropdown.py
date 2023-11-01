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
    pk_url_kwarg = kwargs.get("pk_url_kwarg", "pk")
    all_actions_urls_dict = dict()
    try:
        pk_kwargs = dict()
        if pk_url_kwarg == "slug":
            pk_kwargs.update({"slug": object_var.slug})
        elif pk_url_kwarg == "pk":
            pk_kwargs.update({"pk": object_var.pk})
        if "update" in actions_items:
            all_actions_urls_dict.update(
                {
                    "update": reverse_lazy(
                        f"{actions_base_url}:update", kwargs=pk_kwargs
                    )
                }
            )
        if "details" in actions_items:
            all_actions_urls_dict.update(
                {
                    "details": reverse_lazy(
                        f"{actions_base_url}:details", kwargs=pk_kwargs
                    )
                }
            )
        # keep delete the last one to correct orders in the dropdown menu
        if "delete" in actions_items:
            all_actions_urls_dict.update(
                {
                    "delete": reverse_lazy(
                        f"{actions_base_url}:delete", kwargs=pk_kwargs
                    )
                }
            )

    except:
        pass
    kwargs.update({"action_urls": all_actions_urls_dict})
    return {**context_data, **kwargs}
