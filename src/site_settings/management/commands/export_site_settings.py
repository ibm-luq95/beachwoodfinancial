from django.utils.translation import gettext as _

from core.management.mixins.export_mixin import ExportingCommandMixin
from site_settings.resources.site_settings import SiteSettingsResource
from staff_briefcase.resources.accounts import StaffAccountsResource


class Command(ExportingCommandMixin):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.resources_object = SiteSettingsResource()
        self.app_name = "site_settings"
        self.file_name = "SiteSettings"
        self.help = _("Export site settings for backup")
