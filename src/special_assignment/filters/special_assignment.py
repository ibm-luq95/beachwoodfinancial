# -*- coding: utf-8 -*-#
from core.filters.filter_help_text import HelpfulFilterSet
from special_assignment.models import SpecialAssignmentProxy


class SpecialAssignmentFilter(HelpfulFilterSet):
    class Meta:
        model = SpecialAssignmentProxy
        fields = {
            "title": ["icontains"],
            "client__name": ["exact"],
            "status": ["exact"],
            "assigned_by": ["exact"],
            "is_seen": ["exact"],
        }
