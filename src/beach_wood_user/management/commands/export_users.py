# -*- coding: utf-8 -*-#
from django.utils.translation import gettext as _

from beach_wood_user.resources.users import UsersResource
from core.management.mixins.export_mixin import ExportingCommandMixin


class Command(ExportingCommandMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resources_object = UsersResource()
        self.app_name = "beachwood_user"
        self.file_name = "BWUser"
        self.help = _("Export all users for backup")
