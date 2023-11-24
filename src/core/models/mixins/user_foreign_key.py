# -*- coding: utf-8 -*-#
from django.conf import settings
from django.db import models


class UserForeignKeyMixin(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="%(class)s_related",
    )

    class Meta:
        abstract = True
