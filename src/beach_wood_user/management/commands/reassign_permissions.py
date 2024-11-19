# -*- coding: utf-8 -*-#
import traceback

from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.translation import gettext as _

from beach_wood_user.helpers.permission_helper import PermissionHelper
from beach_wood_user.models import BWUser
from core.management.mixins import CommandStdOutputMixin


# from core.utils import debugging_print


class Command(BaseCommand, CommandStdOutputMixin):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        try:
            verbosity = options.get("verbosity")
            confirm = input(_("Are you sure you want to reassign permissions? [y/n] "))
            if confirm.lower() == "y":
                with transaction.atomic():
                    permissions_codename_list_objs = (
                        PermissionHelper.get_bw_default_permissions(as_list=True)
                    )
                    # DebuggingPrint.pprint(permissions_codename_list_objs)
                    # return
                    users = BWUser.objects.all()
                    for user in users:
                        if verbosity == 2:
                            self.stdout_output(
                                "warn", _(f"Re-assign permissions for {user.email}")
                            )
                        user.user_permissions.clear()
                        user.user_permissions.add(*permissions_codename_list_objs)
                        user.save()

                    self.stdout_output(
                        "success", _("Permissions re-assigned successfully")
                    )
            else:
                self.stdout_output("warn", _("Quit"))
                return
        except Exception:
            self.stdout_output("error", traceback.format_exc())
