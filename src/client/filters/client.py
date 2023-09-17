# -*- coding: utf-8 -*-#

import django_filters
from django import forms
from django.utils.translation import gettext as _

from bookkeeper.models import BookkeeperProxy
from client.models import ClientProxy
from client_category.models import ClientCategory
from core.choices import ImportantContactLabelsEnum
from core.filters.filter_created_mixin import FilterCreatedMixin


class ClientFilter(FilterCreatedMixin):
    form_prefix = "client-filter"
    contact_label = django_filters.ChoiceFilter(
        field_name="important_contacts__contact_label",
        label=_("Contact label"),
        widget=forms.Select,
        choices=ImportantContactLabelsEnum.choices,
        empty_label=_("Contact label"),
    )
    contact_name = django_filters.CharFilter(
        field_name="important_contacts__company_name", label=_("Contact name")
    )
    bookkeepers = django_filters.ModelChoiceFilter(
        field_name="bookkeepers",
        queryset=BookkeeperProxy.objects.all(),
        # widget=forms.Select(attrs={"placeholder": "dsfj"}, emp),
        lookup_expr="exact",
        label=_("Managed by"),
        empty_label=_("Managed by"),
    )
    categories = django_filters.ModelChoiceFilter(
        field_name="categories",
        queryset=ClientCategory.objects.all(),
        # widget=forms.CheckboxSelectMultiple,
        lookup_expr="exact",
        empty_label=_("Categories"),
    )

    class Meta:
        model = ClientProxy
        fields = {
            "name": ["icontains"],
            # "categories": ["exact"],
            "industry": ["icontains"],
            # "important_contacts__company_name": ["icontains"],
            # "important_contacts__contact_label": ["exact"],
            # "created_at": ["exact"]
        }
