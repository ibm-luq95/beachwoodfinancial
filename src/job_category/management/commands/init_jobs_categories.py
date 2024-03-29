# -*- coding: utf-8 -*-#
import traceback

from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.translation import gettext as _
from rich import print
from rich.panel import Panel

from core.init_command_data.job_category import INIT_DATA_JOB_CATEGORIES
from core.management.mixins import CommandStdOutputMixin
from job_category.models import JobCategory


class Command(BaseCommand, CommandStdOutputMixin):
    help = _("Init and seed (fake and dummy) data for job categories")

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                inserted_listed = []
                for category in INIT_DATA_JOB_CATEGORIES:
                    inserted_listed.append(JobCategory(name=category))
                # self.stdout_output("success", _("Done"))
                JobCategory.objects.bulk_create(inserted_listed)
                print(
                    Panel(
                        f"Done, [green]{INIT_DATA_JOB_CATEGORIES}!",
                        title="Success",
                        subtitle="Thank you",
                    )
                )
        except Exception as ex:
            self.stdout_output("error", traceback.format_exc())
