# -*- coding: utf-8 -*-#
import click
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from django.conf import settings
from django.db import transaction
from django.utils import timezone

from core.constants.status_labels import CON_PAST_DUE
from core.utils import bw_log
from job.models import JobProxy


# print(settings.TIME_ZONE)
# print(timezone.now().strftime("%I:%M %p"))


def trigger_fired():
    try:
        with transaction.atomic():
            all_jobs = JobProxy.objects.select_related().all()
            if all_jobs:
                today_date = timezone.now().date()
                # print(today_date, type(today_date))
                for job in all_jobs:
                    if today_date > job.due_date:
                        # print("Bigger ", job.due_date, " --- ", today_date)
                        job.status = CON_PAST_DUE
                        job.save()
                    # else:
                    #     print("Less ****", job.due_date, " --- ", today_date)

    except Exception as ex:
        bw_log().print_exception(suppress=[click], show_locals=False)


def check_past_due_jobs():
    """Check if any jobs are past due."""
    scheduler = BackgroundScheduler()
    cron_trigger = CronTrigger(
        year="*", month="*", day="*", hour=7, minute=0, timezone=settings.TIME_ZONE
    )
    # scheduler.add_job(
    #     trigger_fired,
    #     "cron",
    #     hour=22,
    #     minute=37,
    #     # day="*",
    #     # month="*",
    #     # second="*",
    #     # year="*",
    #     id="check_past_due_jobs",
    #     replace_existing=True,
    #     timezone=settings.TIME_ZONE,
    # )
    scheduler.add_job(
        trigger_fired,
        trigger=cron_trigger,
        id="check_past_due_jobs",
        replace_existing=True,
    )
    scheduler.start()
