# -*- coding: utf-8 -*-#
from django.contrib import admin

from job_category.models import JobCategory
from core.admin import BWBaseAdminModelMixin


@admin.register(JobCategory)
class JobCategoryAdmin(BWBaseAdminModelMixin):
    list_display = ["name", "get_jobs_count", "created_at"]

    @admin.display(description="Jobs")
    def get_jobs_count(self, obj: JobCategory):
        return obj.jobs.count()
