# -*- coding: utf-8 -*-#
import stringcase
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name="to_title_case")
@stringfilter
def to_title_case(text: str) -> str:
    return stringcase.titlecase(text)


@register.filter(name="replace_string")
@stringfilter
def replace_string(text: str) -> str:
    return text.replace("_", " ")
