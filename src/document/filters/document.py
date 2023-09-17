# -*- coding: utf-8 -*-#
from core.filters.filter_created_mixin import FilterCreatedMixin
from document.models import Document


class DocumentFilter(FilterCreatedMixin):
    class Meta:
        model = Document
        fields = {
            "title": ["icontains"],
            "client": ["exact"],
            # "job": ["exact"],
            # "task": ["exact"],
            "document_section": ["exact"],
        }
