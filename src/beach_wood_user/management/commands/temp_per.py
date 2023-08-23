# -*- coding: utf-8 -*-#

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.translation import gettext as _

from beach_wood_user.models import BWUser
from core.constants.users import (
    BOOKKEEPER_GROUP_NAME,
    MANAGER_GROUP_NAME,
    ASSISTANT_GROUP_NAME,
    READONLY_NEW_STAFF_MEMBER_GROUP_NAME,
    DEFAULT_PERMISSIONS_NEW_STAFF_MEMBER,
)
from core.management.mixins import CommandStdOutputMixin
from core.utils import debugging_print


# from core.utils import debugging_print


class Command(BaseCommand, CommandStdOutputMixin):
    def add_arguments(self, parser):
        parser.add_argument(
            "-a",
            "--app-name",
            type=str,
            help=_("Pass app specific name to create group only"),
            required=False,
        )
        parser.add_argument(
            "--clear-all-groups",
            "-ca",
            nargs="?",
            action="store",
            const=True,
            type=str,
            required=False,
            help=_("Delete all groups for manager, bookkeeper, assistant"),
            # default=False,
        )

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                user = BWUser.objects.get(email="gywexygeh@mailinator.com")
                debugging_print(user.groups.all()[1].permissions.all())

        except Exception as ex:
            self.stdout_output("error", str(ex))
