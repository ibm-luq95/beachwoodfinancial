# -*- coding: utf-8 -*-#
import traceback
from django.utils import timezone
from django.core.management.base import BaseCommand
from django.utils.translation import gettext as _

from core.management.mixins import CommandStdOutputMixin


class Command(BaseCommand, CommandStdOutputMixin):
    help = _("Init financial years")

    def handle(self, *args, **options):
        try:
            pass
        except Exception as ex:
            self.stdout_output("error", traceback.format_exc())
