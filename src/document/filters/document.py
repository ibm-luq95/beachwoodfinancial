# -*- coding: utf-8 -*-#
import django_filters
from document.models import Document


class DocumentFilter(django_filters.FilterSet):
    class Meta:
        model = Document
        fields = {
            "title": ["icontains"],
            "client": ["exact"],
            # "job": ["exact"],
            # "task": ["exact"],
            "document_section": ["exact"],
        }
