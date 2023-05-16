# -*- coding: utf-8 -*-#
from django.db import models
from django.utils.translation import gettext as _


class ImportantContactLabelsEnum(models.TextChoices):
    PAYROLL = "payroll", _("Payroll")
    CEO = "ceo", _("CEO")
    OTHER = "other", _("Other")
