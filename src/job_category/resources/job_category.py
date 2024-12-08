# -*- coding: utf-8 -*-#
from import_export import resources

from job_category.models import JobCategory


class JobCategoryResource(resources.ModelResource):
    class Meta:
        model = JobCategory
