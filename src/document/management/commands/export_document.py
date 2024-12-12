# -*- coding: utf-8 -*-#
from django.utils.translation import gettext as _

from core.management.mixins.export_mixin import ExportingCommandMixin
from document.resources.document import DocumentResource


class Command(ExportingCommandMixin):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.resources_object = DocumentResource()
        self.app_name = "document"
        self.file_name = "Document"
        self.help = _("Export documents for backup")
