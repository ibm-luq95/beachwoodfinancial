from django.utils.translation import gettext as _

from core.management.mixins.export_mixin import ExportingCommandMixin
from staff_briefcase.resources.notes import StaffNotesResource


class Command(ExportingCommandMixin):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.resources_object = StaffNotesResource()
        self.app_name = "staff_briefcase"
        self.file_name = "StaffBriefcaseNotes"
        self.help = _("Export staff briefcase notes for backup")
