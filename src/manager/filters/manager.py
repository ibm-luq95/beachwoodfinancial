# -*- coding: utf-8 -*-#
import django_filters
from manager.models import ManagerProxy


class ManagerFilter(django_filters.FilterSet):
    class Meta:
        model = ManagerProxy
        fields = {
            "user__status": ["exact"],
            "user__email": ["exact"],
            "user__is_superuser": ["exact"],
        }
