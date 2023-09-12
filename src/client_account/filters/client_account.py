# -*- coding: utf-8 -*-#
from client_account.models import ClientAccount
from core.filters.filter_help_text import HelpfulFilterSet


class ClientAccountFilter(HelpfulFilterSet):
    class Meta:
        model = ClientAccount
        fields = {
            # "client__name": ["icontains"],
            "account_name": ["icontains"],
            "account_email": ["icontains"],
            "account_url": ["icontains"],
            "status": ["exact"],
        }
