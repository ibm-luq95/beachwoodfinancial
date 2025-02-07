# -*- coding: utf-8 -*-#
from core.filters.filter_created_mixin import FilterCreatedMixin
from special_assignment.models import SpecialAssignmentProxy


class SpecialAssignmentFilter(FilterCreatedMixin):
    class Meta:
        model = SpecialAssignmentProxy
        fields = {
            "title": ["icontains"],
            "client": ["exact"],
            "job": ["exact"],
            "status": ["exact"],
            "assigned_by": ["exact"],
            "is_seen": ["exact"],
        }
