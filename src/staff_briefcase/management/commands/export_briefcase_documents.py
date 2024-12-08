from django.utils.translation import gettext as _

from core.management.mixins.export_mixin import ExportingCommandMixin
from staff_briefcase.resources.accounts import StaffAccountsResource
from staff_briefcase.resources.documents import StaffDocumentsResource


class Command(ExportingCommandMixin):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.resources_object = StaffDocumentsResource()
        self.app_name = "staff_briefcase"
        self.file_name = "StaffBriefcaseDocuments"
        self.help = _("Export staff briefcase documents for backup")
