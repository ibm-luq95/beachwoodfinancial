# -*- coding: utf-8 -*-#
from django.db.models import Q

from core.constants.status_labels import (
    CON_ARCHIVED,
    CON_PAST_DUE,
    CON_COMPLETED,
    CON_IN_PROGRESS,
)
from core.models.querysets import BaseQuerySetMixin
from core.utils import debugging_print


class ClientReportsQuerySet(BaseQuerySetMixin):
    def get_all_past_due_jobs(self) -> BaseQuerySetMixin:
        jobs = self.jobs.filter(Q(status=CON_PAST_DUE))
        return jobs

    def get_all_archived_jobs(self) -> BaseQuerySetMixin:
        jobs = self.jobs.filter(Q(status=CON_ARCHIVED))
        return jobs

    def get_completed_jobs(self) -> BaseQuerySetMixin:
        jobs = self.jobs.filter(Q(status=CON_COMPLETED))
        return jobs

    def get_in_progress_jobs(self) -> BaseQuerySetMixin:
        jobs = self.jobs.filter(Q(status=CON_IN_PROGRESS))
        return jobs

    def get_all_jobs_as_dict(self) -> dict:
        jobs_data = dict()
        clients_jobs = []
        all_clients = self.filter().all()
        for client in all_clients:
            jobs = client.jobs.all()
            clients_jobs.append(
                {"client": client, "jobs": {"count": jobs.count(), "jobs": jobs}}
            )

        debugging_print(clients_jobs)
        return jobs_data
