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
from bookkeeper.models import BookkeeperProxy
from core.choices import JobTypeEnum, JobStateEnum, JobStatusEnum
from core.constants.status_labels import CON_IN_PROGRESS
from core.management.mixins import CommandStdOutputMixin
from django.db.models.functions import TruncYear, ExtractYear, ExtractMonth, TruncMonth
from django.db.models import Count, Sum

from faker import Faker
from client.models import ClientProxy
from core.utils import debugging_print, get_months_abbr
from core.utils.developments.debugging_print_object import BWDebuggingPrint
from job.models import JobProxy
from job_category.models import JobCategory


class Command(BaseCommand, CommandStdOutputMixin):
    help = _("Clients add bookkeepers")

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                all_clients = ClientProxy.objects.all()
                all_bookkeepers = BookkeeperProxy.objects.all()
                for client in all_clients:
                    BWDebuggingPrint.panel(f"Client: {client.name} - {client.pk}")
                    # random_bookkeepers = random.choices(all_bookkeepers, k=2)
                    random_bookkeepers = random.choices(all_bookkeepers, k=random.randint(1, 10))
                    # BWDebuggingPrint.log(f"Random bookkeepers: {random_bookkeepers}")
                    client.bookkeepers.add(*random_bookkeepers)
                    client.save()
                    BWDebuggingPrint.log(
                        "########################################################"
                    )

        except Exception as ex:
            self.stdout_output("error", traceback.format_exc())
