from django.db import models
from django.utils.translation import gettext as _

from core.models.mixins import (
    BaseModelMixin,
    StrModelMixin,
    GeneralStatusFieldMixin,
    GetObjectSectionMixin,
)


class BaseNoteModel(
    BaseModelMixin, GetObjectSectionMixin, GeneralStatusFieldMixin, StrModelMixin
):
    title = models.CharField(_("title"), max_length=60, null=False)
    body = models.TextField(_("body"), null=False)

    class Meta:
        abstract = True
        indexes = [
            models.Index(name="note_title_idx", fields=["title"]),
            models.Index(name="note_body_idx", fields=["body"]),
        ]
