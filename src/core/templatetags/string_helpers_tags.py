# -*- coding: utf-8 -*-#
import stringcase
import textwrap
from django import template
from django.template.defaultfilters import stringfilter

from core.constants.general import DEFAULT_TEMPLATE_TABLE_LIST_TRUNCATED_STRING

register = template.Library()


@register.filter(name="to_title_case")
@stringfilter
def to_title_case(text: str) -> str:
    return stringcase.titlecase(text)


@register.filter(name="replace_string")
@stringfilter
def replace_string(text: str) -> str:
    return text.replace("_", " ")


@register.filter(name="bw_truncate_titles")
@stringfilter
def bw_truncate_titles(text: str) -> str:
    return textwrap.shorten(
        text, width=DEFAULT_TEMPLATE_TABLE_LIST_TRUNCATED_STRING, placeholder="..."
    )


@register.filter(name="grab_last_permission_label")
def grab_last_permission_label(permission_full_name: str) -> str | None:
    if permission_full_name is not None:
        # return " - ".join(permission_full_name.split(" | ")[0:-1])
        return f'{permission_full_name.split(" | ")[0]} - {permission_full_name.split(" | ")[-1]}'
    else:
        return None
