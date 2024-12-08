# -*- coding: utf-8 -*-#
from import_export import resources

from job.models import JobProxy


class JobResource(resources.ModelResource):
    class Meta:
        model = JobProxy
