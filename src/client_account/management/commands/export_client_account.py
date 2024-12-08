# -*- coding: utf-8 -*-#
from django.utils.translation import gettext as _

from client_account.resources.client_account import ClientAccountResource
from core.management.mixins.export_mixin import ExportingCommandMixin


class Command(ExportingCommandMixin):
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resources_object = ClientAccountResource()
        self.app_name = "client account"
        self.file_name = "ClientAccountProxy"
        self.help = _("Export client accounts for backup")
