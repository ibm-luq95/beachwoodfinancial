# -*- coding: utf-8 -*-#
import traceback
import random

from django.utils import timezone
from django.utils.dateparse import parse_date, parse_datetime
from django.utils.timezone import datetime, make_aware
from django.db import transaction

from django.core.management.base import BaseCommand
from django.utils.translation import gettext as _

from beach_wood_user.models import BWUser
from core.choices import JobTypeEnum, JobStateEnum, JobStatusEnum
from core.constants.status_labels import CON_IN_PROGRESS
from core.management.mixins import CommandStdOutputMixin
from django.db.models.functions import TruncYear, ExtractYear, ExtractMonth, TruncMonth
from django.db.models import Count, Sum

from faker import Faker
from client.models import ClientProxy
from core.utils import debugging_print, get_months_abbr
from job.models import JobProxy
from job_category.models import JobCategory


class Command(BaseCommand, CommandStdOutputMixin):
    help = _("Clients seeder")

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            "-n",
            type=int,
            help=_("Number of records"),
            required=False,
            default=1,
        )
        # parser.add_argument(
        #     "--",
        #     "-",
        #     nargs="?",
        #     action="store",
        #     const=True,
        #     type=str,
        #     required=False,
        #     help=_(""),
        #     # default=False,
        # )

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                number = options.get("number")
                # seeder = Seed.seeder("en_US")
                faker = Faker(locale="en_US")
                # jobs = (
                #     JobProxy.objects.annotate(year=ExtractYear("created_at"))
                #     .values("year")
                #     .annotate(count=Count("id"))
                #     .values("year", "count")
                # )
                # jobs = (
                #     JobProxy.objects.annotate(month=ExtractMonth("created_at"))
                #     .values("month")
                #     .annotate(count=Count("id"))
                #     .values("month", "count")
                # )
                # jobs = (
                #     JobProxy.objects.filter(created_at__year="2017")
                #     .annotate(month=ExtractMonth("created_at"))
                #     .values("month")
                #     .annotate(count=Count("id"))
                #     .values("month", "count")
                # )
                jobs = (
                    JobProxy.objects.filter(
                        created_at__year="2020",
                        created_at__month__in=("1", "2", 3, 4, 5, 6, 7, 9, 9, 10, 11, 12),
                        status=CON_IN_PROGRESS,
                    )
                    .annotate(
                        month=ExtractMonth("created_at"), year=ExtractYear("created_at")
                    )
                    .values("month", "year")
                    .annotate(count=Count("id"))
                    .values("month", "year", "count")
                    .order_by("month")
                )
                for job in jobs:
                    debugging_print(job)
                # debugging_print(jobs)

        except Exception as ex:
            self.stdout_output("error", traceback.format_exc())
