# -*- coding: utf-8 -*-#
from django.db import models
from django.utils.translation import gettext as _

from core.choices import StatusEnum


class GeneralStatusFieldMixin(models.Model):
    status = models.CharField(
        _("status"), max_length=10, choices=StatusEnum.choices, default=StatusEnum.ENABLED
    )

    class Meta:
        abstract = True
