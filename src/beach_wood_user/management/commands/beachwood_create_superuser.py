# -*- coding: utf-8 -*-#
import os

from django.contrib.auth.management.commands import createsuperuser
from django.db import transaction
from django.utils.translation import gettext as _

from beach_wood_user.models import BWUser
from core.management.mixins import CommandStdOutputMixin
from core.utils.developments.debugging_print_object import BWDebuggingPrint


class Command(createsuperuser.Command, CommandStdOutputMixin):
    help = _("Create superuser")

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                BWDebuggingPrint.pprint("Creating superuser")
                check = BWUser.objects.filter(email=os.getenv("DJANGO_SUPERUSER_EMAIL"))
                BWDebuggingPrint.print(os.getenv("DJANGO_SUPERUSER_EMAIL"))
                if check:
                    BWDebuggingPrint.panel(
                        f"Superuser exists {os.getenv('DJANGO_SUPERUSER_EMAIL')}"
                    )
                    self.stdout_output("warn", _(f"Superuser exists"))
                    return
                    # quit(0)
                user_data = {
                    "email": os.getenv("DJANGO_SUPERUSER_EMAIL"),
                    "password": os.getenv("DJANGO_SUPERUSER_PASSWORD"),
                    "user_type": os.getenv("DJANGO_SUPERUSER_USER_TYPE"),
                    "user_genre": os.getenv("DJANGO_SUPERUSER_USER_GENRE"),
                }

                self.UserModel._default_manager.db_manager().create_superuser(**user_data)

                if options.get("verbosity", 0) >= 1:
                    self.stdout.write("Superuser created successfully.")
        except Exception as ex:
            BWDebuggingPrint.print_exception()
            self.stdout_output("error", str(ex))
