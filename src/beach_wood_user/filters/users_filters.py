# -*- coding: utf-8 -*-#
import django_filters

from beach_wood_user.models import BWUser


class BWUserFilter(django_filters.FilterSet):
    class Meta:
        model = BWUser
        fields = {
            "first_name": ["icontains"],
            "last_name": ["icontains"],
            "user_type": ["exact"],
            "is_active": ["exact"],
            "is_superuser": ["exact"]
        }
