# -*- coding: utf-8 -*-#
from core.filters.filter_created_mixin import FilterCreatedMixin
from important_contact.models import ImportantContact


class ImportantContactFilter(FilterCreatedMixin):
    class Meta:
        model = ImportantContact
        fields = {
            "contact_first_name": ["icontains"],
            "contact_last_name": ["icontains"],
            "contact_label": ["exact"],
            "company_name": ["icontains"],
        }
