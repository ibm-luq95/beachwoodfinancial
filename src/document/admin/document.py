# -*- coding: utf-8 -*-#
from django.contrib import admin

from document.models import Document
from core.admin import BWBaseAdminModelMixin


@admin.register(Document)
class DocumentAdmin(BWBaseAdminModelMixin):
    pass
