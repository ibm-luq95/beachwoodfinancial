# -*- coding: utf-8 -*-#
from core.filters.filter_created_mixin import FilterCreatedMixin
from task.models import TaskProxy


class TaskFilter(FilterCreatedMixin):
    class Meta:
        model = TaskProxy
        fields = {
            "title": ["icontains"],
            "task_type": ["exact"],
            "status": ["exact"],
            "job": ["exact"],
            # "job__title": ["icontains"],
            "job__managed_by": ["exact"],
            # "job__bookkeeper": ["exact"]
            # "company_name": ["icontains"],
        }
