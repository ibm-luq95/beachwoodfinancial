# -*- coding: utf-8 -*-#
from django.db.models import Q

from core.models.managers import SoftDeleteManager
from special_assignment.models.queryset import SpecialAssignmentQuerySet


class SpecialAssignmentsManager(SoftDeleteManager):
    def get_queryset(self) -> SpecialAssignmentQuerySet:
        queryset = SpecialAssignmentQuerySet(self.model, using=self._db).filter(
            Q(is_deleted=False)
        )
        return queryset
