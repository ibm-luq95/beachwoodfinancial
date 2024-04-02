# -*- coding: utf-8 -*-#
import textwrap

from django.contrib import admin
from django.db import models
from django.utils.translation import gettext as _

from core.models.mixins import BaseModelMixin, StrModelMixin


class StaffNotes(BaseModelMixin, StrModelMixin):
    title = models.CharField(_("title"), max_length=250, null=True, blank=True)
    note = models.TextField(_("Note"))

    @admin.display(description=_("Note body"))
    def note_body(self):
        return textwrap.shorten(self.note, width=20, placeholder="...")

    @admin.display(description=_("briefcase"))
    def get_briefcase(self):
        if hasattr(self, "briefcase"):
            return self.briefcase.get()
        return None

    class Meta:
        verbose_name = _("Staff Note")
        verbose_name_plural = _("Staff Notes")
        ordering = ["title"]
