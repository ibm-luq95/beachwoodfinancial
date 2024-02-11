# -*- coding: utf-8 -*-#
from typing import Any

from django import template

register = template.Library()


@register.filter(name="check_var_none")
def check_var_none(variable: Any) -> bool:
	if variable is None or variable == "":
		return False
	else:
		return True


@register.simple_tag
def render_none_var(
	variable: Any, not_none_value: Any, custom_empty_string: str = "---"
) -> Any | str:
	if variable is None or variable == "":
		return custom_empty_string
	else:
		return not_none_value
