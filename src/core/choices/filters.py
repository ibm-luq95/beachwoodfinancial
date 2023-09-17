# -*- coding: utf-8 -*-#
from django.utils.translation import gettext as _

from django.db import models


class DateFiltersEnum(models.TextChoices):
    PAYROLL = "today", _("Today")
    CEO = "this_week", _("This week")
    OTHER = "this_month", _("This month")
