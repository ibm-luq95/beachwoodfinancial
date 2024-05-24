# -*- coding: utf-8 -*-#
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _


class DueDateOnlyMixin(models.Model):
    """
    Abstract base class that adds a `due_date` field to a model.

    The `due_date` field is a date field that represents the due date of the model.
    It is optional and can be null or blank.

    Attributes:
        due_date (models.DateField): A date field that represents the due date of the model.

    Meta:
        abstract = True: This class is meant to be used as a base class and cannot be instantiated on its own.

    """

    due_date = models.DateField(
        _("due date"),
        default=timezone.now,
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True
