# -*- coding: utf-8 -*-#

from core.filters.filter_help_text import HelpfulFilterSet
from manager.models import ManagerProxy


class ManagerFilter(HelpfulFilterSet):
    class Meta:
        model = ManagerProxy
        fields = {
            "user__status": ["exact"],
            "user__email": ["exact"],
            "user__is_superuser": ["exact"],
        }
