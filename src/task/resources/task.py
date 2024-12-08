# -*- coding: utf-8 -*-#
from import_export import resources

from task.models import TaskProxy


class TaskResource(resources.ModelResource):
    class Meta:
        model = TaskProxy
