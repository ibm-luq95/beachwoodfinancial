# -*- coding: utf-8 -*-#
from django.conf import settings
from django.db import models


class UserForeignKeyMixin(models.Model):
    """
    A mixin class that adds a user foreign key field to a model.

    This mixin provides a ForeignKey field named 'user' that relates to the AUTH_USER_MODEL specified in settings.
    It allows for setting the field as blank and null, and provides a related name for reverse lookups.

    Fields:
        user (ForeignKey): A foreign key to the AUTH_USER_MODEL.

    Meta:
        abstract = True

    """

    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="%(class)s_related",
    )

    class Meta:
        abstract = True
