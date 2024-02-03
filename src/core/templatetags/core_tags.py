# -*- coding: utf-8 -*-#
from datetime import datetime
from typing import Optional, Any
import calendar
import re

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


class SetVarNode(template.Node):
	def __init__(self, new_val, var_name):
		self.new_val = new_val
		self.var_name = var_name

	def render(self, context):
		context[self.var_name] = self.new_val
		return ""


@register.tag
def setvar(parser, token):
	# {% setvar "a string" as new_template_var %}
	# This version uses a regular expression to parse tag contents.
	try:
		# Splitting by None == splitting by spaces.
		tag_name, arg = token.contents.split(None, 1)
	except ValueError:
		raise template.TemplateSyntaxError(
			"%r tag requires arguments" % token.contents.split()[0]
		)
	m = re.search(r"(.*?) as (\w+)", arg)
	if not m:
		raise template.TemplateSyntaxError("%r tag had invalid arguments" % tag_name)
	new_val, var_name = m.groups()
	if not (new_val[0] == new_val[-1] and new_val[0] in ('"', "'")):
		raise template.TemplateSyntaxError(
			"%r tag's argument should be in quotes" % tag_name
		)
	return SetVarNode(new_val[1:-1], var_name)


@register.filter("get_month_abbrev")
def get_month_abbrev(month_index: int) -> str | int:
	try:
		return calendar.month_abbr[month_index]
	except IndexError:
		return month_index


@register.filter("get_var_name")
def get_var_name(var) -> str:
	return type(var).__name__


@register.filter("cast_to_int")
def cast_to_int(value: Any) -> int:
	return int(value)


@register.filter("cast_to_str")
def cast_to_str(value: Any) -> str:
	return str(value)


@register.simple_tag
def define(val=None):
	return val
