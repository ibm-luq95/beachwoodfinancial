# -*- coding: utf-8 -*-#
from django.contrib import admin

from job.models import JobProxy
from core.admin import BWBaseAdminModelMixin


@admin.register(JobProxy)
class JobAdmin(BWBaseAdminModelMixin):
    pass
