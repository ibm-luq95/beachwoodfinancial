# -*- coding: utf-8 -*-#
import calendar

from django.utils.translation import gettext as _

from django.db import models


class DateFiltersEnum(models.TextChoices):
    ALL = "all", _("All")
    TODAY = "today", _("Today")
    THIS_WEEK = "this_week", _("This week")
    THIS_MONTH = "this_month", _("This month")


class DateYearsFiltersEnum(models.IntegerChoices):
    ALL = 0, _("All")
    Y2020 = 2020, _("2020")
    Y2021 = 2021, _("2021")
    Y2022 = 2022, _("2022")
    Y2023 = 2023, _("2023")
    Y2024 = 2024, _("2024")


MONTHS_CHOICES = list()
MONTHS_CHOICES.append(("all", _("All")))
_months_list = list(calendar.month_abbr)
for mon in _months_list:
    if mon != "":
        MONTHS_CHOICES.append((_months_list.index(mon), _(f"{mon}".title())))
