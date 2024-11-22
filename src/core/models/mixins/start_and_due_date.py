# -*- coding: utf-8 -*-#
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _


def get_now_date_only():
    """
    Returns the current date without the time component.

    This function uses the `timezone.now()` method from the `timezone` module to get the current date and time. It then extracts only the date component using the `.date()` method.

    Returns:
        datetime.date: The current date without the time component.

    """
    return timezone.now().date()


class StartAndDueDateMixin(models.Model):
    """
    A mixin class that adds start and due date fields to a model.

    This mixin class adds two date fields to a model: `start_date` and `due_date`.
    The `start_date` field represents the start date of an activity, while the `due_date` field represents the due date of an activity.
    By default, both fields are set to the current date.

    Attributes:
        start_date (DateField): The start date of the activity.
        due_date (DateField): The due date of the activity.

    """

    start_date = models.DateField(
        _("start date"), default=get_now_date_only, null=True, blank=True
    )
    due_date = models.DateField(
        _("due date"), default=get_now_date_only, null=True, blank=True
    )

    class Meta:
        abstract = True
