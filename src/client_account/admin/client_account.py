# -*- coding: utf-8 -*-#
from django.contrib import admin

from client_account.models import ClientAccount
from client_account.resources.client_account import ClientAccountResource
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
    resource_classes = [ClientAccountResource]
