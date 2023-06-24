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
