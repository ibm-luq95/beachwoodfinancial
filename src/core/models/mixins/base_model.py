# -*- coding: utf-8 -*-#

import uuid

from django.db import models
from django.forms.models import model_to_dict
from django.utils import timezone
from django.utils.translation import gettext as _

from core.models.managers import SoftDeleteManager
from core.utils import sort_dict
from .diffing import DiffingMixin


class BaseModelMixin(DiffingMixin, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    metadata = models.JSONField(_("metadata"), null=True, blank=True, default=dict)
    is_deleted = models.BooleanField(_("is deleted"), default=False)
    created_at = models.DateTimeField(
        _("created at"), default=timezone.now, editable=False
    )
    updated_at = models.DateTimeField(
        _("updated at"), auto_now=True, blank=True, null=True, editable=False
    )
    deleted_at = models.DateTimeField(_("deleted at"), null=True, default=None, blank=True)

    objects = SoftDeleteManager()
    # objects = models.Manager()
    original_objects = models.Manager()

    class Meta:
        abstract = True
        # ordering = ["-created_at", "-updated_at"]
        ordering = ["-created_at"]
        permissions = [
            ("can_view_list", "Can view list view"),
            ("view_archive", "Can view archive"),
        ]

    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        self.original_objects.delete()

    def delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.is_deleted = False
        self.deleted_at = None
        self.save()

    @property
    def get_instance_as_dict(self) -> dict:
        data = model_to_dict(self)
        data.setdefault("id", self.id)
        data.setdefault("created_at", self.created_at)
        data.setdefault("updated_at", self.updated_at)
        return sort_dict(data)
