# -*- coding: utf-8 -*-#

from core.filters.filter_help_text import HelpfulFilterSet
from document.models import Document


class DocumentFilter(HelpfulFilterSet):
    class Meta:
        model = Document
        fields = {
            "title": ["icontains"],
            "client": ["exact"],
            # "job": ["exact"],
            # "task": ["exact"],
            "document_section": ["exact"],
        }
