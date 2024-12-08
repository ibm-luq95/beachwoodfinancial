# -*- coding: utf-8 -*-#
from django.utils.translation import gettext as _

from core.management.mixins.export_mixin import ExportingCommandMixin
from discussion.resources.discussion import DiscussionResource


class Command(ExportingCommandMixin):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.resources_object = DiscussionResource()
        self.app_name = "discussion"
        self.file_name = "DiscussionProxy"
        self.help = _("Export discussions for backup")
