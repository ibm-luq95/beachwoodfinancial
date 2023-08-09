# -*- coding: utf-8 -*-#
from discussion.models.discussion import Discussion


class DiscussionProxy(Discussion):

    class Meta:
        proxy = True
