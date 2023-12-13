from core.models.mixins import BaseModelMixin, StrModelMixin
from django.db import models
from django.utils.translation import gettext as _


class TaskItem(BaseModelMixin, StrModelMixin):
    title = models.CharField(_("title"), max_length=100)
    description = models.TextField(_("description"), null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(name="title_idx", fields=["title"]),
            models.Index(name="description_idx", fields=["description"]),
        ]
