# -*- coding: utf-8 -*-#
from django.contrib.auth import get_user_model
from django.db import models


class UserForeignKeyMixin(models.Model):
    user = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="%(class)s_related",
    )

    class Meta:
        abstract = True
