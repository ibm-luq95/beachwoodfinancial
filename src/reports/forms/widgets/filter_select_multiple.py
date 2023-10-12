# -*- coding: utf-8 -*-#
from django.forms.widgets import SelectMultiple

from core.utils import debugging_print


class BWFilterSelectMultipleWidget(SelectMultiple):
    def __init__(self, attrs=None, choices=()):
        super().__init__(attrs)
        self.choices = choices
