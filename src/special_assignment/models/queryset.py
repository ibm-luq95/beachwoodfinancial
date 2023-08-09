# -*- coding: utf-8 -*-#
from django.db.models import Q

from core.constants.status_labels import CON_ARCHIVED
from core.models.querysets import BaseQuerySetMixin


class SpecialAssignmentQuerySet(BaseQuerySetMixin):
    def get_not_seen_special_assignment(self):
        return self.filter(Q(is_seen=False) & ~Q(status__in=[CON_ARCHIVED]))
