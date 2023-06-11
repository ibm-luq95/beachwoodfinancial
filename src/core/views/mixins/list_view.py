# -*- coding: utf-8 -*-#
from django.db.models import Q

from core.constants.status_labels import CON_COMPLETED, CON_ARCHIVED


class BWListViewMixin:
    def get_queryset(self):
        queryset = self.model.objects.filter(~Q(status__in=[CON_COMPLETED, CON_ARCHIVED]))

        return queryset
