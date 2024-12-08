# -*- coding: utf-8 -*-#
from import_export import resources

from discussion.models import DiscussionProxy


class DiscussionResource(resources.ModelResource):
    class Meta:
        model = DiscussionProxy
