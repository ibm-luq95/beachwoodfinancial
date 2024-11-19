# -*- coding: utf-8 -*-#
"""
File: assistant.py
Author: Ibrahim Luqman
Date: 5/10/24

Description: Assistant type choices 
"""
from django.db import models
from django.utils.translation import gettext as _


class AssistantTypeEnum(models.TextChoices):
    ALL = "all", _("All")
    MARKETING = "marketing", _("Marketing")
    ADMIN = "admin", _("Admin")
    BOOKKEEPING = "bookkeeping", _("Bookkeeping")
