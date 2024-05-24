# -*- coding: utf-8 -*-#
from typing import Type

import django_filters
from django.db.models import Field
from django_filters.filters import Filter


class HelpfulFilterSet(django_filters.FilterSet):
    """
    A filter set that provides additional functionality for filtering querysets.

    This class overrides the `filter_for_field` method to modify the filter's help text.

    Methods:
        filter_for_field(cls, f, name, lookup_expr): Overrides the `filter_for_field` method to modify the filter's help text.

    """

    @classmethod
    def filter_for_field(
        cls: Type["HelpfulFilterSet"], f: Field, name: str, lookup_expr: str
    ) -> Filter:
        """
        Overrides the `filter_for_field` method to modify the filter's help text.

        Args:
            f (Field): The field to create a filter for.
            name (str): The name of the filter field.
            lookup_expr (str): The lookup expression for the filter field.

        Returns:
            Filter: The created filter.

        """
        filter: Filter = super().filter_for_field(f, name, lookup_expr)
        if filter.extra.get("help_text"):
            filter.extra["help_text"] = f.help_text

        return filter
