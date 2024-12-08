# -*- coding: utf-8 -*-#
from import_export import resources

from client_account.models import ClientAccount


class ClientAccountResource(resources.ModelResource):
    class Meta:
        model = ClientAccount
