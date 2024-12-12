# -*- coding: utf-8 -*-#
from import_export import resources

from staff_briefcase.models import StaffDocuments


class StaffDocumentsResource(resources.ModelResource):
    class Meta:
        model = StaffDocuments
