# -*- coding: utf-8 -*-#
import django_filters
from django import forms

from task.models import TaskProxy


class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = TaskProxy
        fields = {
            # "task_type": ["exact"],
            "status": ["exact"],
            "title": ["icontains"],
            "job__title": ["icontains"],
            "job__managed_by": ["exact"],
            # "job__bookkeeper": ["exact"]
            # "company_name": ["icontains"],
        }
