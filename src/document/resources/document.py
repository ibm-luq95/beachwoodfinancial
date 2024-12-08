# -*- coding: utf-8 -*-#
from import_export import resources

from document.models import Document


class DocumentResource(resources.ModelResource):
    class Meta:
        model = Document
