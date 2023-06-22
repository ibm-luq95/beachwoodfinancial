# -*- coding: utf-8 -*-#
from django.db import transaction

from task.models import Task


class TaskProxy(Task):
    class Meta:
        proxy = True

    # def log_task_to_history(self) -> None:
    #     with transaction.atomic():
    #         from . import TaskHistory
    #
    #         history_obj, created = TaskHistory.objects.get_or_create(
    #             task=self,
    #             defaults={
    #                 "task": self,
    #                 "previous_status": self.status,
    #                 "is_archived": True,
    #             },
    #         )
    #
    # def unlog_task_from_history(self) -> None:
    #     pass
