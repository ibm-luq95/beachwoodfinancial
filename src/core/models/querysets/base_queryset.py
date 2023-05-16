# -*- coding: utf-8 -*-#
from django.db import models
from django.utils import timezone


class BaseQuerySetMixin(models.QuerySet):
    """
    Prevents objects from being hard-deleted. Instead, sets the
    ``date_deleted``, effectively soft-deleting the object.
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
