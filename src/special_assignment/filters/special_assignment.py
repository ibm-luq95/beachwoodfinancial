# -*- coding: utf-8 -*-#
from special_assignment.models import SpecialAssignmentProxy
import django_filters


class SpecialAssignmentFilter(django_filters.FilterSet):
    class Meta:
        model = SpecialAssignmentProxy
        fields = {
            "title": ["icontains"],
            "client__name": ["exact"],
            "status": ["exact"],
            "assigned_by": ["exact"],
            "is_seen": ["exact"],
        }
