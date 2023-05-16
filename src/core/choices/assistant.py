# -*- coding: utf-8 -*-#
from django.db import models
from django.utils.translation import gettext as _


class AssistantTypeEnum(models.TextChoices):
    ALL = "all", _("All")
    MARKETING = "marketing", _("Marketing")
    ADMIN = "admin", _("Admin")
    BOOKKEEPING = "bookkeeping", _("Bookkeeping")
