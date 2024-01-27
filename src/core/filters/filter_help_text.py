# -*- coding: utf-8 -*-#
import django_filters


class HelpfulFilterSet(django_filters.FilterSet):

    @classmethod
    def filter_for_field(cls, f, name, lookup_expr):
        filter = super(HelpfulFilterSet, cls).filter_for_field(f, name, lookup_expr)
        filter.extra["help_text"] = f.help_text
        return filter
