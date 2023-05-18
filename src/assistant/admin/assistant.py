# -*- coding: utf-8 -*-#
from django.contrib import admin

from assistant.models import AssistantProxy
from core.admin import BWBaseAdminModelMixin


@admin.register(AssistantProxy)
class AssistantAdmin(BWBaseAdminModelMixin):
    list_filter = ["assistant_type"] + BWBaseAdminModelMixin.list_filter
