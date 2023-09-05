# -*- coding: utf-8 -*-#
import django_filters

from bookkeeper.models import BookkeeperProxy


class BookkeeperFilter(django_filters.FilterSet):
    class Meta:
        model = BookkeeperProxy
        fields = {
            # "title": ["icontains"],
            # "client": ["exact"],
            # "job": ["exact"],
            # "task": ["exact"],
            # "document_section": ["exact"],
        }
