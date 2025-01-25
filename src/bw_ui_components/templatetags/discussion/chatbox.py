# -*- coding: utf-8 -*-#
from django import template

from core.utils import get_request_context
from core.utils.developments.debugging_print_object import DebuggingPrint

register = template.Library()


@register.inclusion_tag("bw_ui_components/discussion/chatbox.html", takes_context=True)
def bw_discussion_chatbox(context, *args, **kwargs) -> dict:
    context_data = get_request_context(context, kwargs)
    DebuggingPrint.print(kwargs)
    return {**context_data, **kwargs}
