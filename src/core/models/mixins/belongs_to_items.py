from django.db import models

from client.models import ClientProxy
from core.models.fields import CustomForeignKey
from job.models import JobProxy
from task.models import TaskProxy


class BelongsToItemsMixin(models.Model):
    """Mixin for models that belong to items"""

    client = CustomForeignKey(
        to=ClientProxy,
        on_delete=models.SET_NULL,
        related_name="%(class)s",
        null=True,
        blank=True,
    )
    job = CustomForeignKey(
        to=JobProxy,
        on_delete=models.SET_NULL,
        related_name="%(class)s",
        null=True,
        blank=True,
    )
    task = CustomForeignKey(
        to=TaskProxy,
        on_delete=models.SET_NULL,
        related_name="%(class)s",
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True
        indexes = [
            models.Index(name="job_related_items_idx", fields=["job"]),
            models.Index(name="task_related_items_idx", fields=["task"]),
            models.Index(name="client_related_items_idx", fields=["client"]),
        ]
