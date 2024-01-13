# -*- coding: utf-8 -*-#

import uuid
from typing import Optional

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _

from core.models.managers import SoftDeleteManager
from .diffing import DiffingMixin
from .get_model_instance_as_dict import GetModelInstanceAsDictMixin
from ..managers.archive_manager import ArchiveManager


class BaseModelMixin(DiffingMixin, GetModelInstanceAsDictMixin, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    metadata = models.JSONField(
        _("metadata"), null=True, blank=True, default=dict, editable=False
    )
    is_deleted = models.BooleanField(_("is deleted"), default=False, editable=False)
    created_at = models.DateTimeField(
        _("created at"), default=timezone.now, editable=False
    )
    updated_at = models.DateTimeField(
        _("updated at"), auto_now=True, blank=True, null=True, editable=False
    )
    deleted_at = models.DateTimeField(
        _("deleted at"), null=True, default=None, blank=True, editable=False
    )

    objects = SoftDeleteManager()
    original_objects = models.Manager()
    archive_objects = ArchiveManager()

    class Meta:
        abstract = True
        # ordering = ["-created_at", "-updated_at"]
        # ordering = ["-created_at"]
        permissions = [
            ("can_view_list", "Can view list view"),
            ("view_archive", "Can view archive"),
        ]

    @classmethod
    def get_columns_names(
        cls, fields: Optional[list | tuple] = None, excluded: Optional[list | tuple] = None
    ) -> list | tuple:
        columns_names = []
        excluded_fields = ["id", "metadata", "deleted_at", "updated_at", "is_deleted"]
        if excluded is not None:
            excluded_fields = excluded_fields + excluded
        for field in cls._meta.get_fields():
            if field.name not in excluded_fields:
                columns_names.insert(0, field.verbose_name)
        return columns_names

    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        self.original_objects.delete()

    def delete(self):
        self.soft_delete()

    def restore(self):
        self.is_deleted = False
        self.deleted_at = None
        self.save()
