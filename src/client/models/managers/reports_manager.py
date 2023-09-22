# -*- coding: utf-8 -*-#
from django.db.models import Q

from client.models.querysets.reports_qs import ClientReportsQuerySet
from core.models.managers import SoftDeleteManager


class ClientReportsManager(SoftDeleteManager):
    def get_queryset(self) -> ClientReportsQuerySet:
        queryset = ClientReportsQuerySet(self.model, using=self._db).filter(
            Q(is_deleted=False)
        )
        return queryset

    def get_all_jobs_as_dict(self) -> dict:
        qs = self.get_queryset()

        return qs.get_all_jobs_as_dict()
