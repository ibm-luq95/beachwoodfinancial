# -*- coding: utf-8 -*-#
import django_filters
from django import forms

from core.filters.filter_help_text import HelpfulFilterSet
from core.utils.developments.debugging_print_object import DebuggingPrint
from job.models import JobProxy
from job_category.models import JobCategory
from django.utils.translation import gettext as _


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
        # widget=forms.CheckboxSelectMultiple,
        widget=forms.SelectMultiple(attrs={"data_name": "job-categories"}),
        lookup_expr="exact",
    )
    show_all = django_filters.BooleanFilter(
        label=_("Show all jobs"),
        method="filter_show_all",
        help_text=_("Check this box to show all jobs."),
    )

    def filter_show_all(self, queryset, name, value):
        """Custom filter to return all jobs if 'show_all' is checked."""
        if value:  # If the checkbox is checked (True)
            return JobProxy.original_objects.all()  # Return all jobs
        return queryset  # Otherwise, return the filtered queryset

    class Meta:
        model = JobProxy
        # form = JobFilterForm
        fields = {
            "title": ["icontains"],
            "managed_by": ["exact"],
            "period_year": ["exact"],
            "period_month": ["exact"],
            # "bookkeeper": ["icontains"],
            "client": ["exact"],
            # "job_type": ["exact"],
            "status": ["exact"],
            "state": ["exact"],
            # "categories": ["exact"],
            # "due_date": ["gt", "lt"],
        }
