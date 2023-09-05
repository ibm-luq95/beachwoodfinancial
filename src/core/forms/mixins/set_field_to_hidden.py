# -*- coding: utf-8 -*-#
from typing import Optional

from django import forms


class SetFieldsInputsHiddenMixin:
    def __init__(self, hidden_inputs: Optional[dict] = None):
        if hidden_inputs is not None:
            field_names: list = hidden_inputs.get("field_names")
            for field_name in field_names:
                self.fields[field_name].widget = forms.HiddenInput()
