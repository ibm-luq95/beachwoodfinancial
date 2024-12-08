# -*- coding: utf-8 -*-#
from import_export import resources

from client_category.models import ClientCategory


class ClientCategoryResource(resources.ModelResource):
    class Meta:
        model = ClientCategory
