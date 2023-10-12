# -*- coding: utf-8 -*-#
import traceback
from django.core.management.base import BaseCommand
from django.utils.translation import gettext as _

from core.management.mixins import CommandStdOutputMixin


class Command(BaseCommand, CommandStdOutputMixin):
    help = _("Generate and initilaize reports permissions")

    def add_arguments(self, parser):
        parser.add_argument(
            "--apps-names", "-an", type=str, help=_("Apps name"), required=False
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
            pass
        except Exception as ex:
            self.stdout_output("error", traceback.format_exc())
