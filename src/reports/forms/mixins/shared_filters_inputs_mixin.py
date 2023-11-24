# -*- coding: utf-8 -*-#
from django.utils import timezone
from django.utils.translation import gettext as _

from django import forms
from django.db import models

from core.choices.filters import DateFiltersEnum, DateYearsFiltersEnum, MONTHS_CHOICES


class SharedFilterInputsMixin(forms.Form):
    quick_created_at = forms.ChoiceField(
        label=_("Quick created at"),
        required=False,
        choices=DateFiltersEnum.choices,
        initial=DateFiltersEnum.ALL,
    )
    created_at = forms.DateField(
        label=_("Created at"),
        widget=forms.DateInput(attrs={"type": "date"}),
        required=False,
        help_text=_("Created at"),
    )
    created_year = forms.ChoiceField(
        label=_("Created year"),
        required=False,
        choices=DateYearsFiltersEnum.choices,
        help_text=_("Creation year"),
        initial=DateYearsFiltersEnum.Y2023,
    )

    # months = forms.ChoiceField(
    #     label=_("Months"),
    #     required=False,
    #     choices=MONTHS_CHOICES,
    #     help_text=_("Months"),
    #     widget=forms.SelectMultiple,
    # )

    def serialize_inputs(self) -> dict:
        data = dict()
        # print(self.data)
        for name, field in self.fields.items():
            data[name] = self.fields[name].initial

        return data
