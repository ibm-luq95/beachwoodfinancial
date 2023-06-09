# -*- coding: utf-8 -*-#
from datetime import datetime
from typing import Optional

from django import template
from django.core.paginator import Paginator
from django.utils import timezone
from django import template
from django.template import Node, Variable, VariableDoesNotExist

from core.constants.general import DEFAULT_FULL_DATE_TIME_FORMAT

register = template.Library()


@register.filter(name="get_paginator_object")
def get_paginator_object(objects_list) -> Paginator:
    return Paginator(objects_list, 1)


@register.simple_tag
def now_timestamp(date_and_time: Optional[str] = None) -> timezone:
    if date_and_time is None:
        date_and_time = timezone.now()
    else:
        date_and_time = datetime.strptime(date_and_time, DEFAULT_FULL_DATE_TIME_FORMAT)

    timestamp = datetime.timestamp(date_and_time)
    return timestamp


class MyCustomTagNode(Node):
    def __init__(self, value):
        self.value = value

    def render(self, context):
        print("##############################3")
        context["my_variable"] = self.value
        return ""


@register.simple_tag(name="my_custom_tag")
def my_custom_tag(value):
    return MyCustomTagNode(value)
