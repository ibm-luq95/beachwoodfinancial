# -*- coding: utf-8 -*-#
from django.contrib import admin

from client.models import ClientProxy
from core.admin import BWBaseAdminModelMixin


@admin.register(ClientProxy)
class ClientAdmin(BWBaseAdminModelMixin):
    pass
