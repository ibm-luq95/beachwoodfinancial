# -*- coding: utf-8 -*-#
from django.utils.translation import gettext as _

from client_category.resources.client_category import ClientCategoryResource
from core.management.mixins.export_mixin import ExportingCommandMixin


class Command(ExportingCommandMixin):
    def __init__(self,  *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.resources_object = ClientCategoryResource()
        self.app_name = "client category"
        self.file_name = "ClientCategory"
        self.help = _("Export client categories for backup")
