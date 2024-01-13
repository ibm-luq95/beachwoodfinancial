# -*- coding: utf-8 -*-#
from django.contrib import admin

from client_account.models import ClientAccount
from core.admin import BWBaseAdminModelMixin


@admin.register(ClientAccount)
class ClientAccountAdmin(BWBaseAdminModelMixin):
    list_display = [
        "client",
        "service_name",
        "account_name",
        "is_services",
        "account_username",
        "status",
    ]
