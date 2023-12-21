# -*- coding: utf-8 -*-#
from random import randint

from django.db import models
from django.db.models import Q
from django.db.models.aggregates import Count

from core.constants.status_labels import CON_COMPLETED, CON_ARCHIVED
from core.models.querysets import BaseQuerySetMixin


class SoftDeleteManager(models.Manager):
    ALLOWED_STATUS = [CON_ARCHIVED, CON_COMPLETED]

    def get_queryset(self) -> BaseQuerySetMixin:
        queryset = BaseQuerySetMixin(self.model, using=self._db).filter(
            Q(is_deleted=False)
        )

        return queryset

    def all(self) -> BaseQuerySetMixin:
        qs = self.get_queryset()
        field_names = [field.name for field in self.model._meta.fields]
        if "status" in field_names:
            qs = qs.filter(~Q(status__in=self.ALLOWED_STATUS))
        return qs

    def random(self):
        count = self.aggregate(count=Count("id"))["count"]
        random_index = randint(0, count - 1)
        return self.all()[random_index]
