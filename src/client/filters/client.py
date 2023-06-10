# -*- coding: utf-8 -*-#
import django_filters
from django import forms

from bookkeeper.models import BookkeeperProxy
from client.models import ClientProxy
from client_category.models import ClientCategory


class ClientFilter(django_filters.FilterSet):
    bookkeepers = django_filters.ModelMultipleChoiceFilter(
        field_name="bookkeepers",
        queryset=BookkeeperProxy.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        lookup_expr="exact",
        label="Managed by",
    )
    categories = django_filters.ModelMultipleChoiceFilter(
        field_name="categories",
        queryset=ClientCategory.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        lookup_expr="exact",
    )

    class Meta:
        model = ClientProxy
        fields = {
            "name": ["icontains"],
            # "categories": ["exact"],
            "industry": ["icontains"],
            "important_contacts__company_name": ["icontains"],
            "important_contacts__contact_label": ["exact"],
        }
