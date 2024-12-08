# -*- coding: utf-8 -*-#
from django.utils.translation import gettext as _

from bookkeeper.resources.bookkeeper import BookkeeperResource
from core.management.mixins.export_mixin import ExportingCommandMixin


class Command(ExportingCommandMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resources_object = BookkeeperResource()
        self.app_name = "bookkeeper"
        self.file_name = "BookkeeperProxy"
        self.help = _("Export bookkeepers for backup")
