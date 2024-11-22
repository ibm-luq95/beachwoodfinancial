# -*- coding: utf-8 -*-#

from django.core.management.base import BaseCommand
from django.utils.translation import gettext as _

from django.db import transaction

from beach_wood_user.models import BWUser
from core.management.mixins import CommandStdOutputMixin
from core.utils.developments.debugging_print_object import DebuggingPrint
from core.utils.developments.debugging_prompt import DebuggingPrompt
from staff_briefcase.models import StaffBriefcase


class Command(BaseCommand, CommandStdOutputMixin):

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                cnfm = DebuggingPrompt.confirm(_("Are you sure want to start?"))
                if cnfm is True:
                    self.stdout_output("info", _("Initializing staff briefcase..."))
                    users = BWUser.objects.all()
                    for user in users:

                        if StaffBriefcase.objects.filter(user=user).exists():
                            DebuggingPrint.pprint(
                                _(f"Staff briefcase already exists for user {user}.")
                            )
                        else:
                            DebuggingPrint.pprint(
                                _("Creating staff briefcase for: %s") % user
                            )
                            StaffBriefcase.objects.get_or_create(user=user)
                else:
                    return

        except Exception as ex:
            self.stdout_output("error", str(ex))
