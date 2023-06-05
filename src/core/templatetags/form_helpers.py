# -*- coding: utf-8 -*-#
from django import template
from django import forms

register = template.Library()


@register.filter(name="get_form_field_type")
def get_form_field_type(field) -> str:
    # if isinstance(field, forms.ChoiceField):
    #     return "ChoiceField"
    return type(field).__name__
