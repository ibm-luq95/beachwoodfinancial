# -*- coding: utf-8 -*-#
from django.contrib import admin

from job_category.models import JobCategory
from core.admin import BWBaseAdminModelMixin


@admin.register(JobCategory)
class JobCategoryAdmin(BWBaseAdminModelMixin):
    pass
