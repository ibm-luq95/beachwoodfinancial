# -*- coding: utf-8 -*-#
from django.contrib import admin

from core.admin import BWBaseAdminModelMixin
from discussion.models import DiscussionProxy


@admin.register(DiscussionProxy)
class DiscussionAdmin(BWBaseAdminModelMixin):
    pass
