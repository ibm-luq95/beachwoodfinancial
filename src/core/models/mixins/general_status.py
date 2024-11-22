# -*- coding: utf-8 -*-#
from django.db import models
from django.utils.translation import gettext as _

from core.choices import StatusEnum


class GeneralStatusFieldMixin(models.Model):
    """
    A mixin class that adds a `status` field to a model.

    This mixin class provides a `status` field to the model, which can be used to track the status of the model instance.
    The `status` field is a `CharField` with a maximum length of 10 characters and a default value of `StatusEnum.ENABLED`.
    The available choices for the `status` field are defined by the `StatusEnum` enumeration.

    Attributes:
    - status: A `CharField` representing the status of the model instance.

    """

    status = models.CharField(
        _("status"), max_length=10, choices=StatusEnum.choices, default=StatusEnum.ENABLED
    )

    class Meta:
        abstract = True
