# -*- coding: utf-8 -*-#
import django_filters
from django import forms

from core.filters.filter_help_text import HelpfulFilterSet
from job.models import JobProxy
from job_category.models import JobCategory


class JobFilter(HelpfulFilterSet):
    due_date = django_filters.DateFilter(
        field_name="due_date", widget=forms.DateInput(attrs={"type": "date"})
    )
    due_date__gt = django_filters.DateFilter(
        field_name="due_date",
        widget=forms.DateInput(attrs={"type": "date"}),
        lookup_expr="gt",
    )
    due_date__lt = django_filters.DateFilter(
        field_name="due_date",
        widget=forms.DateInput(attrs={"type": "date"}),
        lookup_expr="lt",
    )
    categories = django_filters.ModelMultipleChoiceFilter(
        field_name="categories",
        queryset=JobCategory.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        lookup_expr="exact",
    )

    # bookkeeper = django_filters.ChoiceFilter(
    #     widget=forms.Select(), choices=get_all_bookkeepers_as_choices
    # )

    class Meta:
        model = JobProxy
        # form = JobFilterForm
        fields = {
            "title": ["icontains"],
            "managed_by": ["exact"],
            # "bookkeeper": ["icontains"],
            "client__name": ["icontains"],
            # "job_type": ["exact"],
            "status": ["exact"],
            "state": ["exact"],
            # "categories": ["exact"],
            # "due_date": ["gt", "lt"],
        }
        # fields = [
        #     "title",
        #     # "bookkeeper__user__first_name",
        #     # "bookkeeper__user__last_name",
        #     "bookkeeper__user",
        #     "client__name",
        #     "job_type",
        #     "status",
        #     "due_date",
        # ]
