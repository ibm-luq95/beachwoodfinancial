# -*- coding: utf-8 -*-#

from cfo.models import CFOProxy
from core.filters.filter_created_mixin import FilterCreatedMixin


class CFOFilter(FilterCreatedMixin):
    class Meta:
        model = CFOProxy
        fields = {
            # "title": ["icontains"],
            # "client": ["exact"],
            # "job": ["exact"],
            # "task": ["exact"],
            # "document_section": ["exact"],
            "user__is_active": ["exact"],
        }
