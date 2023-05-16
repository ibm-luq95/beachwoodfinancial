# -*- coding: utf-8 -*-#
from datetime import datetime
from typing import Optional

from django import template
from django.core.paginator import Paginator
from django.utils import timezone

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
