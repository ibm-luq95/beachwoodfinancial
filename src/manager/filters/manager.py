# -*- coding: utf-8 -*-#
from core.filters.filter_created_mixin import FilterCreatedMixin
from manager.models import ManagerProxy


class ManagerFilter(FilterCreatedMixin):
    class Meta:
        model = ManagerProxy
        fields = {
            "user__status": ["exact"],
            "user__email": ["exact"],
            "user__is_superuser": ["exact"],
        }
