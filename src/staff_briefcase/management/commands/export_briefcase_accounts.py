from django.utils.translation import gettext as _

from core.management.mixins.export_mixin import ExportingCommandMixin
from staff_briefcase.resources.accounts import StaffAccountsResource


class Command(ExportingCommandMixin):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.resources_object = StaffAccountsResource()
        self.app_name = "staff_briefcase"
        self.file_name = "StaffBriefcaseAccounts"
        self.help = _("Export staff briefcase accounts for backup")
