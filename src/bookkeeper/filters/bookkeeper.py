# -*- coding: utf-8 -*-#
import django_filters

from bookkeeper.models import BookkeeperProxy
from core.filters.filter_created_mixin import FilterCreatedMixin


class BookkeeperFilter(FilterCreatedMixin):
    class Meta:
        model = BookkeeperProxy
        fields = {
            # "title": ["icontains"],
            # "client": ["exact"],
            # "job": ["exact"],
            # "task": ["exact"],
            # "document_section": ["exact"],
        }
