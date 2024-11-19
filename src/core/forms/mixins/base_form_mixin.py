# -*- coding: utf-8 -*-#
from typing import Any

from core.forms.mixins.html5_mixin import Html5Mixin
from django import forms


class BWBaseFormMixin(Html5Mixin, forms.Form):
    """
    A mixin class that provides common functionality for form classes.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Initializes the BWBaseFormMixin instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super(BWBaseFormMixin, self).__init__(*args, **kwargs)
