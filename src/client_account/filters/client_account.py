# -*- coding: utf-8 -*-#
import django_filters
from client_account.models import ClientAccount


class ClientAccountFilter(django_filters.FilterSet):
    class Meta:
        model = ClientAccount
        fields = {
            # "client__name": ["icontains"],
            "account_name": ["icontains"],
            "account_email": ["icontains"],
            "account_url": ["icontains"],
            "status": ["exact"],
        }
