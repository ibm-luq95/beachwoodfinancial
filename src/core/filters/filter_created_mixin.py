# -*- coding: utf-8 -*-#
from datetime import timedelta

import django_filters
from django.utils import timezone
from django.utils.translation import gettext as _

from core.choices.filters import DateFiltersEnum
from core.filters.filter_help_text import HelpfulFilterSet


class FilterCreatedMixin(HelpfulFilterSet):
    created = django_filters.ChoiceFilter(
        field_name="created_at",
        choices=DateFiltersEnum.choices,
        method="filter_created",
        empty_label=_("---"),
    )
    created_between = django_filters.DateFromToRangeFilter(
        field_name="created_at",
        widget=django_filters.widgets.RangeWidget(
            attrs={"placeholder": "YYYY/MM/DD", "type": "date"}
        ),
        label=_("Created between"),
    )

    def filter_created(self, queryset, name, value):
        date = None
        # breakpoint()
        # construct the full lookup expression.
        if value == "today":
            date = timezone.now()
            return queryset.filter(created_at__date=date)

        elif value == "this_week":
            now = timezone.now()
            start = now - timedelta(days=now.weekday())
            end = start + timedelta(days=6)
            # debugging_print(queryset.filter(created_at__date__range=(start.date(), end.date())))
            return queryset.filter(created_at__date__range=(start.date(), end.date()))
        elif value == "this_month":
            now = timezone.now()
            return queryset.filter(created_at__month=now.month, created_at__year=now.year)
        else:
            return queryset.none()

        # debugging_print(date.weekday())
        # return queryset.filter(**{lookup: False})
        # return queryset.filter(created_at__date=date)
        # return queryset.none()

        # alternatively, you could opt to hardcode the lookup. e.g.,
        # return queryset.filter(published_on__isnull=False)
