# -*- coding: utf-8 -*-#
from import_export import resources

from staff_briefcase.models import StaffBriefcase


class StaffBriefcaseResource(resources.ModelResource):
    class Meta:
        model = StaffBriefcase
