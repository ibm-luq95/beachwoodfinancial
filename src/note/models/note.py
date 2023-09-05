from django.db import models
from django.utils.translation import gettext as _

from client.models import ClientProxy
from core.choices import NoteSectionEnum
from core.models.mixins import (
    BaseModelMixin,
    GetObjectSectionMixin,
    GeneralStatusFieldMixin,
    StrModelMixin,
)
from job.models import JobProxy
from task.models import TaskProxy


class Note(BaseModelMixin, GetObjectSectionMixin, GeneralStatusFieldMixin, StrModelMixin):
    """Notes model for bookkeeper, assistant, and manager

    Args:
        BaseModelMixin (models.Model): Django base model mixin
    """

    title = models.CharField(_("title"), max_length=60, null=False)
    body = models.TextField(_("body"), null=False)
    client = models.ForeignKey(
        to=ClientProxy,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="notes",
    )
    job = models.ForeignKey(
        to=JobProxy, on_delete=models.SET_NULL, null=True, blank=True, related_name="notes"
    )
    task = models.ForeignKey(
        to=TaskProxy,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="notes",
    )
    note_section = models.CharField(
        _("note section"),
        max_length=15,
        null=True,
        blank=True,
        choices=NoteSectionEnum.choices,
        editable=False,
        db_index=True,
    )

    class Meta(BaseModelMixin.Meta):
        verbose_name_plural = "notes"

    def save(self, *args, **kwargs):
        if self.job:
            self.note_section = NoteSectionEnum.JOB
        elif self.task:
            self.note_section = NoteSectionEnum.TASK
        elif self.client:
            self.note_section = NoteSectionEnum.CLIENT
        super().save(*args, **kwargs)
