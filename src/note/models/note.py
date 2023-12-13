from django.db import models
from django.utils.translation import gettext as _

from core.choices import NoteSectionEnum
from core.models.mixins.belongs_to_items import BelongsToItemsMixin
from note.models.base_abstract_note import BaseNoteModel


class Note(BaseNoteModel, BelongsToItemsMixin):
    """Notes model for bookkeeper, assistant, and manager

    Args:
        BaseModelMixin (models.Model): Django base model mixin
    """

    note_section = models.CharField(
        _("note section"),
        max_length=15,
        null=True,
        blank=True,
        choices=NoteSectionEnum.choices,
        editable=False,
        db_index=True,
    )

    class Meta:
        verbose_name_plural = "notes"
        indexes = [
            models.Index(name="note_section_idx", fields=["note_section"]),
        ]

    def save(self, *args, **kwargs):
        if self.job:
            self.note_section = NoteSectionEnum.JOB
        elif self.task:
            self.note_section = NoteSectionEnum.TASK
        elif self.client:
            self.note_section = NoteSectionEnum.CLIENT
        super().save(*args, **kwargs)
