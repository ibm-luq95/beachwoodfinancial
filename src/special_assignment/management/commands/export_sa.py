# -*- coding: utf-8 -*-#
from django.utils.translation import gettext as _

from core.management.mixins.export_mixin import ExportingCommandMixin
from special_assignment.resources.special_assignment import SpecialAssignmentResource
from task.resources.task import TaskResource


class Command(ExportingCommandMixin):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.resources_object = SpecialAssignmentResource()
        self.app_name = "special_assignment"
        self.file_name = "SpecialAssignmentProxy"
        self.help = _("Export special assignments for backup")
