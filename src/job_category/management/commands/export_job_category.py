# -*- coding: utf-8 -*-#
from django.utils.translation import gettext as _

from core.management.mixins.export_mixin import ExportingCommandMixin
from job_category.resources.job_category import JobCategoryResource


class Command(ExportingCommandMixin):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.resources_object = JobCategoryResource()
        self.app_name = "job_category"
        self.file_name = "JobCategory"
        self.help = _("Export job category for backup")
