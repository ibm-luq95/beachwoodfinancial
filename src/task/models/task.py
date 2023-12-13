# -*- coding: utf-8 -*-#

from django.db import models
from django.utils.translation import gettext as _

from core.choices import TaskStatusEnum, TaskTypeEnum
from core.models.mixins import BaseModelMixin, StrModelMixin
from core.models.mixins.access_proxy_models_mixin import AccessProxyModelMixin
from core.models.mixins.cron_column_mixin import CronColumnMixin
from job.models.job_proxy import JobProxy
from task.models.base_abstract_task import BaseTaskModel


# class Task(BaseModelMixin, StartAndDueDateMixin, StrModelMixin, CreatedByMixin):
class Task(BaseTaskModel):
    """Tasks for every job

    Args:
        BaseModelMixin (models.Model): The base django model mixin
    """

    # def __init__(self, *args, **kwargs):
    #     super(Task, self).__init__(*args, **kwargs)
    #     self.__original_model = self.model

    job = models.ForeignKey(
        to=JobProxy,
        on_delete=models.PROTECT,
        related_name="tasks",
        null=True,
        blank=True,
        db_index=True,
    )

    class Meta:
        indexes = [
            models.Index(name="task_job_idx", fields=["job"]),
        ]
