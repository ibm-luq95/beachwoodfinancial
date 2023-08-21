# -*- coding: utf-8 -*-#
import django_filters

from assistant.models import AssistantProxy


class AssistantFilter(django_filters.FilterSet):
    class Meta:
        model = AssistantProxy
        fields = {
            "assistant_type": ["exact"],
            "user__status": ["exact"],
            "user__email": ["exact"],
        }
