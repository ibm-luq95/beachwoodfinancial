# -*- coding: utf-8 -*-#
from django import forms
from django.utils.translation import gettext as _


class StartAndDueDateFilterInputMixin(forms.Form):
    start_date = forms.DateField(
        label=_("Start date"),
        widget=forms.DateInput(attrs={"type": "date"}),
        required=False,
        help_text=_("Start date"),
    )
    end_date = forms.DateField(
        label=_("End date"),
        widget=forms.DateInput(attrs={"type": "date"}),
        required=False,
        help_text=_("End date"),
    )
