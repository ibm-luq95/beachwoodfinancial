# -*- coding: utf-8 -*-#

from core.filters.filter_help_text import HelpfulFilterSet
from task.models import TaskProxy


class TaskFilter(HelpfulFilterSet):
    class Meta:
        model = TaskProxy
        fields = {
            # "task_type": ["exact"],
            "status": ["exact"],
            "title": ["icontains"],
            # "job__title": ["icontains"],
            "job": ["exact"],
            "job__managed_by": ["exact"],
            # "job__bookkeeper": ["exact"]
            # "company_name": ["icontains"],
        }
