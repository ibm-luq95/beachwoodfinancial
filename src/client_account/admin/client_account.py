# -*- coding: utf-8 -*-#
from django.contrib import admin

from client_account.models import ClientAccount
from core.admin import BWBaseAdminModelMixin


@admin.register(ClientAccount)
class ClientAccountAdmin(BWBaseAdminModelMixin):
    pass
