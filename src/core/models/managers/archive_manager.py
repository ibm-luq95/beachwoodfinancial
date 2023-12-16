# -*- coding: utf-8 -*-#
from random import randint

from django.db import models
from django.db.models import Q

from core.constants.status_labels import CON_ARCHIVED, CON_COMPLETED
from core.models.querysets import BaseQuerySetMixin


class ArchiveManager(models.Manager):
    ALLOWED_STATUS = [CON_ARCHIVED, CON_COMPLETED]

    def get_queryset(self) -> BaseQuerySetMixin:
        queryset = (
            BaseQuerySetMixin(self.model, using=self._db)
            .filter(Q(is_deleted=False) & Q(status__in=self.ALLOWED_STATUS))
            .order_by("-created_at")
        )

        return queryset

    def all(self) -> BaseQuerySetMixin:
        """
        Returns a `BaseQuerySetMixin` object representing all instances of the model
        with a status of either `CON_ARCHIVED` or `CON_COMPLETED`, ordered by `created_at` in descending order.

        :return: A `BaseQuerySetMixin` object representing all instances of the model with the specified statuses.
        :rtype: BaseQuerySetMixin
        """
        qs = self.get_queryset()

        return qs
