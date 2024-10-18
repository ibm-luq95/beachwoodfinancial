# -*- coding: utf-8 -*-#
from django.db.models.base import ModelBase
from django.db.models.signals import post_save

from core.constants.status_labels import CON_ARCHIVED, CON_COMPLETED
from job.helpers import JobArchiveRelatedItemsHelper
from job.models import JobProxy, Job


def archive_job_items_signal(
    sender: ModelBase, instance: Job | JobProxy, created: bool, **kwargs
):
    if created is False:
        helper = JobArchiveRelatedItemsHelper(job_object=instance)
        new_status = instance.status
        if new_status == CON_ARCHIVED or new_status == CON_COMPLETED:
            pass


post_save.connect(archive_job_items_signal, sender=JobProxy)
post_save.connect(archive_job_items_signal, sender=Job)
