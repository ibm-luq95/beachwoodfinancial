# -*- coding: utf-8 -*-#
import traceback

from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.translation import gettext as _
from faker import Faker
import random

from beach_wood_user.models import BWUser
from core.choices import BeachWoodUserStatusEnum
from core.management.mixins import CommandStdOutputMixin
from core.utils.developments.debugging_print_object import BWDebuggingPrint
from core.utils.developments.debugging_print_types import DPOTableOptions
from core.utils.developments.debugging_prompt import DebuggingPrompt


class Command(BaseCommand, CommandStdOutputMixin):
    help = _("Init and seed (fake and dummy) users only for development")
    USER_TYPES_LIST = ["all", "bookkeeper", "assistant", "manager"]

    def add_arguments(self, parser):
        parser.add_argument(
            "--user-type",
            "-t",
            type=str,
            help=_("User type (bookkeeper, assistant, manager)"),
            required=True,
        )
        parser.add_argument(
            "--number",
            "-n",
            type=int,
            default=1,
            required=False,
            help=_("Number of records"),
        )

    def handle(self, *args, **options):
        try:
            dprint = BWDebuggingPrint()
            with transaction.atomic():
                number = options.get("number")
                user_type = options.get("user_type")
                if user_type not in self.USER_TYPES_LIST:
                    self.stdout_output(
                        "error", _(f"User type must be one of {self.USER_TYPES_LIST}")
                    )
                    return
                if user_type == "all":
                    dprint.log(_(f"Will create all user types: {self.USER_TYPES_LIST}"))

                faker = Faker(locale="en_US")

                created_users = []
                for i in range(0, number, 1):
                    fake_data = {
                        "password": "test123456",
                        "first_name": faker.first_name(),
                        "last_name": faker.last_name(),
                        "email": faker.ascii_free_email(),
                        "user_genre": "user",
                        "status": random.choice(BeachWoodUserStatusEnum.choices)[0],
                    }
                    if user_type != "all":
                        fake_data.update({"user_type": user_type})
                    else:
                        fake_data.update(
                            {
                                "user_type": faker.random_element(
                                    ["bookkeeper", "assistant", "manager"]
                                )
                            }
                        )
                    user = BWUser.objects.create(**fake_data)
                    created_users.append(user)

                rows = []
                for user in created_users:
                    rows.append(
                        [
                            str(user.id),
                            user.first_name,
                            user.last_name,
                            user.email,
                            user.user_type,
                            user.status,
                            ":white_check_mark:" if user.is_active else ":X:",
                        ]
                    )
                # dprint.pprint(rows)
                table_options: DPOTableOptions = {
                    "caption": "Created users",
                    "title": "New users",
                    "safe_box": True,
                    "show_lines": True,
                }
                table = dprint.table(
                    columns_headers=[
                        "Id",
                        "First name",
                        "Last name",
                        "Email",
                        "User type",
                        "Status",
                        "Active",
                    ],
                    rows=rows,
                    table_options=table_options,
                    return_table=True,
                )
                dprint.panel(text_content=table, title="Created users")
                self.stdout_output("success", _(f"Users created successfully!"))

        except Exception as ex:
            self.stdout_output("error", traceback.format_exc())
