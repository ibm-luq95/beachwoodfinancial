# -*- coding: utf-8 -*-#
from import_export import resources

from special_assignment.models import SpecialAssignmentProxy


class SpecialAssignmentResource(resources.ModelResource):
    class Meta:
        model = SpecialAssignmentProxy
