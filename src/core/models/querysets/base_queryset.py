# -*- coding: utf-8 -*-#
from django.db import models
from django.utils import timezone


class BaseQuerySetMixin(models.QuerySet):
    """
    BaseQuerySetMixin class extends the Django models.QuerySet class.

    Methods:
        - delete(self): Sets the `deleted_at` attribute of each object in the queryset to the current time and sets the `is_deleted` attribute to True.
        - restore(self): Sets the `deleted_at` attribute of each object in the queryset to None and sets the `is_deleted` attribute to False.

    """

    def delete(self):
        for obj in self:
            obj.deleted_at = timezone.now()
            obj.is_deleted = True
            obj.save()

    def restore(self):
        for obj in self:
            obj.deleted_at = None
            obj.is_deleted = False
            obj.save()
