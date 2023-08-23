# -*- coding: utf-8 -*-#

from django.utils.translation import gettext as _

from core.constants.status_labels import CON_COMPLETED
from special_assignment.models.special_assignment import SpecialAssignment


class SpecialAssignmentProxy(SpecialAssignment):
    class Meta(SpecialAssignment.Meta):
        proxy = True

    def get_is_seen_label(self) -> str:
        if self.is_seen is True:
            return _("Seen")
        else:
            return _("Not seen")

    def is_completed(self) -> bool:
        if self.status == CON_COMPLETED:
            return True
        else:
            return False
