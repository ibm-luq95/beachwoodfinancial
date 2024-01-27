# -*- coding: utf-8 -*-#
import traceback
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.translation import gettext as _

from core.management.mixins import CommandStdOutputMixin
from core.utils.developments.debugging_print_object import BWDebuggingPrint
from core.utils.developments.debugging_prompt import DebuggingPrompt
from job.models import JobProxy


class Command(BaseCommand, CommandStdOutputMixin):
    help = _("Init job months and years periods")

    def handle(self, *args, **options):
        try:
            all_jobs = JobProxy.objects.all()
            cnfm = DebuggingPrompt.confirm(_("Are you sure want to start?"))
            if cnfm is True:
                with transaction.atomic():
                    for job in all_jobs:
                        BWDebuggingPrint.pprint(job.created_at)
            else:
                return
        except Exception as ex:
            self.stdout_output("error", traceback.format_exc())
