# -*- coding: utf-8 -*-#
from typing import Optional

from django import forms


class BWPasswordInputWidget(forms.widgets.PasswordInput):
    """
    Custom password input widget for Beach Wood Financial forms.

    Attributes:
        attrs (Optional[dict]): Optional attributes for the password input widget.

    """

    def __init__(self, attrs: Optional[dict] = None, *args, **kwargs):
        """
        Initializes the BWPasswordInputWidget instance.

        Args:
            attrs: Optional attributes for the password input widget. Defaults to None.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        """
        attrs = attrs or {}
        attrs.update({"class": "input", "autocomplete": "new-password"})
        super(BWPasswordInputWidget, self).__init__(attrs)
