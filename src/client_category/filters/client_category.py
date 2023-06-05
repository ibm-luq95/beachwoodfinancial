# -*- coding: utf-8 -*-#
import django_filters
from client_category.models import ClientCategory


class ClientCategoryFilter(django_filters.FilterSet):
    class Meta:
        model = ClientCategory
        fields = {
            "name": ["icontains"],
            "status": ["exact"],
        }
