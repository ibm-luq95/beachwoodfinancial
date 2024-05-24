# -*- coding: utf-8 -*-#
"""
File: development_tags.py
Author: Ibrahim Luqman
Date: 5/13/24

Description: Templatetags only used in development stage.
"""
from typing import Any

from django import template

from core.utils import debugging_print

register = template.Library()


@register.filter(name="get_var_type")
def get_var_type(var: Any) -> str:
    """
    Get the type of the variable.

    Args:
        var (Any): The variable to get the type of.

    Returns:
        str: The type of the variable as a string.

    """
    return str(type(var))


@register.filter(name="dir_var")
def dir_var(var: Any) -> None:
    """
    Print the directory listing of the variable.

    Args:
        var (Any): The variable to print the directory listing of.

    """
    debugging_print(dir(var))
