# -*- coding: utf-8 -*-#

from core.filters.filter_help_text import HelpfulFilterSet
from important_contact.models import ImportantContact


class ImportantContactFilter(HelpfulFilterSet):
    class Meta:
        model = ImportantContact
        fields = {
            "contact_first_name": ["icontains"],
            "contact_last_name": ["icontains"],
            "contact_label": ["exact"],
            "company_name": ["icontains"],
        }
