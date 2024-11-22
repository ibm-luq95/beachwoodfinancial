# -*- coding: utf-8 -*-#
"""
File: important_contact.py
Author: Ibrahim Luqman
Date: 5/10/24

Description: Important contact app's choices
"""
from django.db import models
from django.utils.translation import gettext as _


class ImportantContactLabelsEnum(models.TextChoices):
    PAYROLL = "payroll", _("Payroll")
    CEO = "ceo", _("CEO")
    OTHER = "other", _("Other")
