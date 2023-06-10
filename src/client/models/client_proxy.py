# -*- coding: utf-8 -*-#
from django.db import transaction
from django.db.models import Q

from client.models import Client
from core.constants.status_labels import (
    CON_ARCHIVED,
    CON_COMPLETED,
    CON_DISABLED,
    CON_ENABLED,
    CON_NOT_STARTED,
)


class ClientProxy(Client):
    class Meta:
        proxy = True

    def get_managed_bookkeepers(self) -> set | None:
        all_bookkeepers = []
        jobs = self.jobs.all()
        if jobs:
            for job in jobs:
                # print(job)
                for bookkeeper in job.bookkeeper.all():
                    all_bookkeepers.append(bookkeeper)
            return set(all_bookkeepers)
        else:
            return None

    def get_all_tasks(self) -> list | None:
        all_tasks = []
        jobs = self.jobs.all()
        if jobs:
            for job in jobs:
                tasks = job.tasks.all()
                if tasks:
                    for task in tasks:
                        all_tasks.append(task)
        return all_tasks

    def archive_all_items(self) -> None:
        with transaction.atomic():
            tasks = self.get_all_tasks()
            documents = self.documents.select_related().all()
            notes = self.notes.select_related().all()
            jobs = self.jobs.select_related().all()
            company_services = self.company_services.select_related().all()
            special_assignments = self.special_assignments.select_related().all()

            if (
                self.status == CON_ARCHIVED
                or self.status == CON_COMPLETED
                or self.status == CON_DISABLED
            ):
                # Set notes to archived
                if notes:
                    notes.update(status=CON_ARCHIVED)
                # Set documents to archived
                if documents:
                    documents.update(status=CON_ARCHIVED)
                # Set tasks to archived
                if tasks:
                    for task in tasks:
                        task.status = CON_ARCHIVED
                        task.save()
                # Set company services to archived
                if company_services:
                    company_services.update(status=CON_ARCHIVED)

                # Set jobs to archived
                if jobs:
                    jobs.update(status=CON_ARCHIVED)

                # Set special assignments to archived
                if special_assignments:
                    special_assignments.update(status=CON_ARCHIVED)
            else:
                # Set notes to enabled
                if notes:
                    notes.filter(Q(status=CON_ARCHIVED)).update(status=CON_ENABLED)
                # Set documents to enabled
                if documents:
                    documents.filter(Q(status=CON_ARCHIVED)).update(status=CON_ENABLED)
                # Set tasks to archived
                if tasks:
                    for task in tasks:
                        task.status = CON_NOT_STARTED
                        task.save()
                # Set company services to enabled
                if company_services:
                    company_services.filter(Q(status=CON_ARCHIVED)).update(
                        status=CON_ENABLED
                    )
                # Set special assignments to not started
                if special_assignments:
                    special_assignments.filter(Q(status=CON_ARCHIVED)).update(
                        status=CON_NOT_STARTED
                    )
