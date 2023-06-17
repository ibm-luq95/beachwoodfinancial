# -*- coding: utf-8 -*-#
from django import template
from django import forms
from django.forms import BoundField, Field, Widget
from django.forms.models import ModelMultipleChoiceField
from django.utils.safestring import SafeString

from core.utils import debugging_print

register = template.Library()


@register.filter(name="bw_get_form_field_type")
def bw_get_form_field_type(field) -> str:
    # if isinstance(field, forms.ChoiceField):
    #     return "ChoiceField"
    return type(field).__name__


@register.filter(name="bw_add_state_css_class")
def bw_add_state_css_class(input_bound_field: BoundField, state: str) -> SafeString:
    filed: Field = input_bound_field.field
    css_classes: str = filed.widget.attrs.get("class", None)
    if css_classes:
        css_classes: list = css_classes.split(" ")
    else:
        css_classes: list = []
    if state == "error":
        css_classes.append("border-red-500")
        css_classes.append("focus:border-red-500")
        css_classes.append("focus:ring-red-500")
    elif state == "success":
        css_classes.append("border-green-500")
        css_classes.append("focus:border-green-500")
        css_classes.append("focus:ring-green-500")
    return input_bound_field.as_widget(attrs={"class": " ".join(css_classes)})


@register.simple_tag(takes_context=True)
def bw_testing_form_field(context, input_bound_field: BoundField) -> None:
    # debugging_print(dir(input_bound_field))
    # debugging_print(input_bound_field, is_inspect=True)
    # debugging_print(input_bound_field.data)
    # debugging_print(input_bound_field.value())
    # debugging_print(type(input_bound_field))
    # debugging_print(dir(input_bound_field.widget))
    # checkboxselectmultiple
    # widget_type = input_bound_field.widget_type
    # field_obj: ModelMultipleChoiceField | Field = input_bound_field.field
    # debugging_print(dir(field_obj))
    # debugging_print(field_obj.bound_data)
    # debugging_print(input_bound_field.label)
    # debugging_print(dir(field_obj.choices))
    # debugging_print(input_bound_field.css_classes())
    # for item in field_obj.choices:
    #     choice_value, choice_label = item
    #     debugging_print(type(choice_value))
    #     debugging_print(dir(choice_value))
    #     debugging_print(f"{choice_value.instance} -> Instance")
    #     debugging_print(f"{choice_value.value} -> Value")
    # debugging_print(dir(field_obj))

    return ""