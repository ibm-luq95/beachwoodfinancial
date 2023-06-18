# -*- coding: utf-8 -*-#
import secrets

from django.db import models
from django.utils.translation import gettext as _

from client.models import ClientProxy
from core.choices import DocumentTypesEnum
from core.models.mixins import BaseModelMixin, GeneralStatusFieldMixin, StrModelMixin


def saved_document_file_path(instance, filename):
    file_suffix = secrets.token_urlsafe(7)
    return f"documents/{file_suffix}_{filename}"


class Document(BaseModelMixin, GeneralStatusFieldMixin, StrModelMixin):
    title = models.CharField(
        _("title"), max_length=70, null=False, blank=False, db_index=True
    )
    document_section = models.CharField(
        _("document section"),
        max_length=15,
        null=True,
        blank=True,
        choices=DocumentTypesEnum.choices,
        db_index=True,
    )
    document_file = models.FileField(
        _("document file"), upload_to=saved_document_file_path
    )

    client = models.ForeignKey(
        to=ClientProxy,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="documents",
    )
    # job = models.ForeignKey(
    #     to=JobProxy, on_delete=models.SET_NULL, null=True, blank=True, related_name="documents"
    # )
    # task = models.ForeignKey(
    #     to=TaskProxy, on_delete=models.SET_NULL, null=True, blank=True, related_name="documents"
    # )

    # def delete(self, *args, **kwargs):
    #     self.document_file.storage.delete(self.document_file.name)
    #     super(Documents, self).delete(*args, **kwargs)
