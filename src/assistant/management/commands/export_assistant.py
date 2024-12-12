# -*- coding: utf-8 -*-#
from django.utils.translation import gettext as _

from assistant.resources.assistant import AssistantResource
from core.management.mixins.export_mixin import ExportingCommandMixin


class Command(ExportingCommandMixin):
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resources_object = AssistantResource()
        self.app_name = "assistant"
        self.file_name = "AssistantProxy"
        self.help = _("Export assistant for backup")
