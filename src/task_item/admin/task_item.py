# -*- coding: utf-8 -*-#
from django.contrib import admin

from core.admin import BWBaseAdminModelMixin
from task_item.models import TaskItem


@admin.register(TaskItem)
class TaskItemAdmin(BWBaseAdminModelMixin):
	pass
