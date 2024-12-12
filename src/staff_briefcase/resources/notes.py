# -*- coding: utf-8 -*-#
from import_export import resources

from staff_briefcase.models import StaffNotes


class StaffNotesResource(resources.ModelResource):
    class Meta:
        model = StaffNotes
