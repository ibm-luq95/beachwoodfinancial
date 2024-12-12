# -*- coding: utf-8 -*-#

from django.utils.translation import gettext as _

from core.management.mixins.export_mixin import ExportingCommandMixin
from job.resources.jobs import JobResource


class Command(ExportingCommandMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resources_object = JobResource()
        self.app_name = "job"
        self.file_name = "JobProxy"
        self.help = _("Export jobs for backup")
