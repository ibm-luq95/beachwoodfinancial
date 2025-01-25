# -*- coding: utf-8 -*-#
from django.contrib import admin

from client_category.models import ClientCategory
from core.admin import BWBaseAdminModelMixin


@admin.register(ClientCategory)
class ClientCategoryAdmin(BWBaseAdminModelMixin):
    list_display = ["name", "get_clients_count", "created_at"]

    @admin.display(description="Clients")
    def get_clients_count(self, obj: ClientCategory):
        return obj.clients.count()
