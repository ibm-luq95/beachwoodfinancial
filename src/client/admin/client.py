# -*- coding: utf-8 -*-#
from django.contrib import admin

from client.models import ClientProxy
from core.admin import BWBaseAdminModelMixin


@admin.register(ClientProxy)
class ClientAdmin(BWBaseAdminModelMixin):
    list_display = ("name", "email", "industry", "status", "created_at")
    list_filter = ["status", "industry"] + BWBaseAdminModelMixin.list_filter
    search_fields = ("email",)
