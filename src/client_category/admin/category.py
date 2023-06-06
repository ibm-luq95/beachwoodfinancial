# -*- coding: utf-8 -*-#
from django.contrib import admin

from client_category.models import ClientCategory
from core.admin import BWBaseAdminModelMixin


@admin.register(ClientCategory)
class ClientCategoryAdmin(BWBaseAdminModelMixin):
    pass
