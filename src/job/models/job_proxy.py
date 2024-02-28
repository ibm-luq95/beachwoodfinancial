# -*- coding: utf-8 -*-#
from django.db import transaction
from django.db.models import Q, Manager

from bookkeeper.models import BookkeeperProxy
from core.constants.status_labels import (
    CON_ARCHIVED,
    CON_COMPLETED,
    CON_ENABLED,
    CON_NOT_STARTED,
)
from core.utils import debugging_print
from job.models import Job


class JobProxy(Job):
    # objects = Manager()  # This only enable when import using django-import-export package

    class Meta(Job.Meta):
        proxy = True

    def unplug_bookkeeper_for_client_finished_job(self):
        managed_by = self.managed_by
        if self.status == CON_COMPLETED or self.status == CON_ARCHIVED:
            if managed_by:
                with transaction.atomic():
                    client = self.client
                    if hasattr(managed_by, "bookkeeper"):
                        bookkeeper_obj = managed_by.bookkeeper
                        # debugging_print(bookkeeper_obj)
                        bookkeeper_obj = BookkeeperProxy.objects.get(pk=bookkeeper_obj.pk)
                        client.bookkeepers.remove(bookkeeper_obj)
                        client.save()
                        # debugging_print(self.model_class())
                        JobProxy.objects.filter(pk=self.pk).update(managed_by=None)
