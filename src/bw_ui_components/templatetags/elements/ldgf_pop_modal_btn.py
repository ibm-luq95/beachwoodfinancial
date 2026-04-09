# -*- coding: utf-8 -*-#
from django import template

from core.utils import get_request_context

register = template.Library()


@register.inclusion_tag(
    "bw_ui_components/modals/create_btn_ldgf_pop_modal.html", takes_context=True
)
def ldgf_pop_modal_btn(context, *args, **kwargs) -> dict:
    context_data = get_request_context(context, kwargs)
    return {**context_data, **kwargs}
