# -*- coding: utf-8 -*-#
from typing import Optional

from django import forms


class SetFieldsInputsHiddenMixin:
    """
    A mixin class that provides functionality to set the inputs of specified fields to
    hidden.
    """

    def __init__(self, hidden_inputs: Optional[dict] = None):
        """
        Initializes the SetFieldsInputsHiddenMixin instance.

        Args:
            hidden_inputs: A dictionary containing information about the hidden inputs.
                The dictionary should have the following keys:
                - field_names: A list of field names to set as hidden inputs.
            hidden_inputs: Optional[dict]. Defaults to None.

        """
        if hidden_inputs is not None:
            field_names: list = hidden_inputs.get("field_names")
            for field_name in field_names:
                self.fields[field_name].widget = forms.HiddenInput()
