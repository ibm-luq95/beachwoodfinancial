# -*- coding: utf-8 -*-#
from random import randint

from django.db import models
from django.db.models import Q
from django.db.models.aggregates import Count

from core.models.querysets import BaseQuerySetMixin


class SoftDeleteManager(models.Manager):
    def get_queryset(self) -> BaseQuerySetMixin:
        queryset = BaseQuerySetMixin(self.model, using=self._db).filter(
            Q(is_deleted=False)
        )

        return queryset

    def random(self):
        count = self.aggregate(count=Count("id"))["count"]
        random_index = randint(0, count - 1)
        return self.all()[random_index]
