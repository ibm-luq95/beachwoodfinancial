# -*- coding: utf-8 -*-#
import secrets
from django.contrib import admin
from django.utils.translation import gettext as _
from django.db import models

from core.models.mixins import BaseModelMixin


def saved_document_file_path(instance, filename):
    file_suffix = secrets.token_urlsafe(7)
    return f"staff_documents/{file_suffix}_{filename}"


class StaffDocuments(BaseModelMixin):
    title = models.CharField(_("title"), max_length=250, null=True, blank=True)
    document_file = models.FileField(
        _("document file"), upload_to=saved_document_file_path
    )

    @admin.display(description=_("briefcase"))
    def get_briefcase(self):
        if hasattr(self, "briefcase"):
            return self.briefcase.get()
        return None

    class Meta:
        verbose_name = _("Staff Document")
        verbose_name_plural = _("Staff Documents")
