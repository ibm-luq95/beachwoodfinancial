# -*- coding: utf-8 -*-#
from django.contrib import admin

from core.admin import BWBaseAdminModelMixin
from special_assignment.models import SpecialAssignmentProxy


@admin.register(SpecialAssignmentProxy)
class SpecialAssignmentAdmin(BWBaseAdminModelMixin):
    pass
