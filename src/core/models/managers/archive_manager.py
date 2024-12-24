# -*- coding: utf-8 -*-#

from django.db import models
from django.db.models import Q

from core.constants.status_labels import CON_ARCHIVED, CON_COMPLETED
from core.models.querysets import BaseQuerySetMixin


class ArchiveManager(models.Manager):
    """
    A manager for handling archived instances of a model.

    This manager provides methods for querying and managing instances of a model
    that are archived or completed. It extends the base Django `Manager` class
    to include additional functionality specific to archived data.

    Methods:
        get_queryset(self) -> BaseQuerySetMixin:
            Returns a queryset of all instances of the model that are archived
            or completed, ordered by `created_at` in descending order.
    """

    ALLOWED_STATUS = [CON_ARCHIVED, CON_COMPLETED]

    def get_queryset(self) -> BaseQuerySetMixin:
        """
        Returns a `BaseQuerySetMixin` object representing all instances of the model that
        are not marked as deleted, with a status of either `CON_ARCHIVED` or
        `CON_COMPLETED`, ordered by `created_at` in descending order.

        Returns:
            BaseQuerySetMixin: A `BaseQuerySetMixin` object representing all instances of the model with the specified statuses.

        """
        queryset = (
            BaseQuerySetMixin(self.model, using=self._db)
            .filter(Q(is_deleted=False) & Q(status__in=self.ALLOWED_STATUS))
            .order_by("-created_at")
        )

        return queryset

    def all(self) -> BaseQuerySetMixin:
        """
        Returns a `BaseQuerySetMixin` object representing all instances of the model with a
        status of either `CON_ARCHIVED` or `CON_COMPLETED`, ordered by `created_at` in
        descending order.

        Returns:
            BaseQuerySetMixin: A `BaseQuerySetMixin` object representing all instances of the model with the specified statuses.

        """
        qs = self.get_queryset()

        return qs
