# -*- coding: utf-8 -*-#
from django.contrib import admin

from task.models import TaskProxy
from core.admin import BWBaseAdminModelMixin
from task.resources.task import TaskResource


@admin.register(TaskProxy)
class TaskAdmin(BWBaseAdminModelMixin):
    list_display = ("title", "job", "status", "task_type", "updated_by_cron", "created_at")
    resource_classes = [TaskResource]
