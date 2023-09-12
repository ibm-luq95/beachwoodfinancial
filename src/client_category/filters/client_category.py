# -*- coding: utf-8 -*-#
from client_category.models import ClientCategory
from core.filters.filter_help_text import HelpfulFilterSet


class ClientCategoryFilter(HelpfulFilterSet):
    class Meta:
        model = ClientCategory
        fields = {"name": ["icontains"], "status": ["exact"]}
