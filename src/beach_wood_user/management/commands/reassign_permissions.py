# -*- coding: utf-8 -*-#
import traceback

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.translation import gettext as _

from beach_wood_user.helpers.permission_helper import PermissionHelper
from beach_wood_user.models import BWUser
from core.constants.users import DEFAULT_PERMISSIONS_NEW_STAFF_MEMBER
from core.management.mixins import CommandStdOutputMixin
from core.utils import debugging_print


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
                        PermissionHelper.get_bw_default_permissions(as_form_choices=True)
                    )
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
        except Exception as ex:
            self.stdout_output("error", traceback.format_exc())
