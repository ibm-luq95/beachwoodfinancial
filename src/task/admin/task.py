# -*- coding: utf-8 -*-#
from django.contrib import admin

from task.models import TaskProxy
from core.admin import BWBaseAdminModelMixin


@admin.register(TaskProxy)
class TaskAdmin(BWBaseAdminModelMixin):
    list_display = ("title", "status", "task_type", "created_at")
