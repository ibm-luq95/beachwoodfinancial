# -*- coding: utf-8 -*-#
from django.contrib import admin

from core.admin import BWBaseAdminModelMixin
from fiscal_year.models import FiscalYear


@admin.register(FiscalYear)
class FiscalYearAdmin(BWBaseAdminModelMixin):
    pass
