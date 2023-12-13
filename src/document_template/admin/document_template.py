# -*- coding: utf-8 -*-#
from django.contrib import admin

from core.admin import BWBaseAdminModelMixin
from document_template.models import DocumentTemplate


@admin.register(DocumentTemplate)
class DocumentTemplateAdmin(BWBaseAdminModelMixin):
    pass
