# -*- coding: utf-8 -*-#
import django_filters

from assistant.models import AssistantProxy
from core.filters.filter_created_mixin import FilterCreatedMixin


class AssistantFilter(FilterCreatedMixin):
    class Meta:
        model = AssistantProxy
        fields = {
            "assistant_type": ["exact"],
            "user__status": ["exact"],
            "user__email": ["exact"],
        }
