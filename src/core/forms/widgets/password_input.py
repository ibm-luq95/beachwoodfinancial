# -*- coding: utf-8 -*-#
from typing import Optional

from django import forms


class CustomPasswordInputWidget(forms.widgets.PasswordInput):
    def __init__(self, attrs: Optional[dict] = None, *args, **kwargs):
        attrs = attrs or {}
        attrs.update({"class": "input", "autocomplete": "new-password"})
        super(CustomPasswordInputWidget, self).__init__(attrs)
