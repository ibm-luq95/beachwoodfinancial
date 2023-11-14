# -*- coding: utf-8 -*-#
import random
import traceback

from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.translation import gettext as _
from faker import Faker

from core.choices import (
    TaskStatusEnum,
    TaskTypeEnum,
)
from core.management.mixins import CommandStdOutputMixin
from core.utils import debugging_print
from job.models import JobProxy
from task.models import TaskProxy


class Command(BaseCommand, CommandStdOutputMixin):
    help = _("Tasks seeder")

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            "-n",
            type=int,
            help=_("Number of records"),
            required=False,
            default=1,
        )

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                number = options.get("number")
                # seeder = Seed.seeder("en_US")
                faker = Faker(locale="en_US")
                all_jobs = JobProxy.objects.all()
                if all_jobs.count() == 0:
                    raise Exception(_("No jobs found"))

                for i in range(0, number, 1):
                    fake_data = {
                        # "client": random.choice(all_clients),
                        "job": random.choice(all_jobs),
                        "title": faker.job(),
                        "additional_notes": faker.sentence(nb_words=15),
                        "hints": random.choice([None, faker.sentence(nb_words=5)]),
                        "task_type": random.choice(TaskTypeEnum.choices)[0],
                        "status": random.choice(TaskStatusEnum.choices)[0],
                        "created_at": faker.date_time_between_dates(
                            datetime_start="-4y", datetime_end="-1y"
                        ),
                        # "start_date": faker.date_between(
                        #     # start_date="-1y", end_date="today"
                        #     start_date="-2d",
                        #     end_date="-1d",
                        # ),
                        # "due_date": faker.date_between(start_date="-1y", end_date="today"),
                        # "due_date": faker.date_between(start_date="+4d", end_date="+5d"),
                    }
                    new_task = TaskProxy.objects.create(**fake_data)
                    # debugging_print(new_task.categories.all())
                    new_task.save()
                    debugging_print(f"{new_task.title} - created successfully!")

        except Exception as ex:
            self.stdout_output("error", traceback.format_exc())
