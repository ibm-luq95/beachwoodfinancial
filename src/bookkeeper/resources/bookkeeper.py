# -*- coding: utf-8 -*-#
from import_export import resources

from bookkeeper.models import BookkeeperProxy


class BookkeeperResource(resources.ModelResource):
    class Meta:
        model = BookkeeperProxy
