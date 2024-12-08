# -*- coding: utf-8 -*-#
from django.utils.translation import gettext as _

from core.management.mixins.export_mixin import ExportingCommandMixin
from task.resources.task import TaskResource


class Command(ExportingCommandMixin):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.resources_object = TaskResource()
        self.app_name = "task"
        self.file_name = "TasksProxy"
        self.help = _("Export tasks for backup")
