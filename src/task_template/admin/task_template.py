# -*- coding: utf-8 -*-#
from django.contrib import admin

from core.admin import BWBaseAdminModelMixin
from task_template.models import TaskTemplate


@admin.register(TaskTemplate)
class TaskTemplateAdmin(BWBaseAdminModelMixin):
	list_display = ("title", "status", "task_type", "updated_by_cron", "created_at")
