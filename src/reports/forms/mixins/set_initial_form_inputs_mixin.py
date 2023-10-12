# -*- coding: utf-8 -*-#
from typing import Optional

from django.http import HttpRequest
from django import forms

from core.utils import debugging_print


class SetInitialFilterFormInputsMixin:
    def __init__(self, request: Optional[HttpRequest] = None):
        for name, field in self.fields.items():
            if isinstance(field.widget, forms.SelectMultiple) or isinstance(
                field.widget, forms.CheckboxSelectMultiple
            ):
                field.widget.attrs["data-filter-input-type"] = "multiple"
            else:
                field.widget.attrs["data-filter-input-type"] = "single"

        if hasattr(request, "GET"):
            if bool(request.GET):
                for name, value in request.GET.items():
                    # self.fields[name].initial = value
                    if value:
                        field_obj = self.fields.get(name)
                        if hasattr(field_obj, "widget"):
                            widget = field_obj.widget
                            filter_input_type = widget.attrs.get("data-filter-input-type")
                            if filter_input_type:
                                if filter_input_type == "multiple":
                                    self.fields[name].initial = request.GET.getlist(name)
                                elif filter_input_type == "single":
                                    self.fields[name].initial = request.GET.get(name)
