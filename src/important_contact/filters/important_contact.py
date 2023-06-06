# -*- coding: utf-8 -*-#
import django_filters
from important_contact.models import ImportantContact


class ImportantContactFilter(django_filters.FilterSet):
    class Meta:
        model = ImportantContact
        fields = {
            "contact_first_name": ["icontains"],
            "contact_last_name": ["icontains"],
            "contact_label": ["exact"],
            "company_name": ["icontains"],
        }
