# -*- coding: utf-8 -*-#

from django.utils.translation import gettext as _

from core.constants.status_labels import CON_COMPLETED
from special_assignment.models.special_assignment import SpecialAssignment


class SpecialAssignmentProxy(SpecialAssignment):
    """Proxy model for SpecialAssignment.

    This class is a proxy model that inherits from SpecialAssignment. It provides additional methods for retrieving the label for the is_seen attribute and checking if the assignment is completed.

    Attributes:
        None

    Methods:
        get_is_seen_label(self) -> str: Returns the label for the is_seen attribute.
        is_completed(self) -> bool: Checks if the assignment is completed based on the status attribute.
    """

    class Meta(SpecialAssignment.Meta):
        proxy = True

    def get_is_seen_label(self) -> str:
        """Returns the label for the is_seen attribute.

        If the is_seen attribute is True, returns "Seen". Otherwise, returns "Not seen".

        Returns:
            str: The label for the is_seen attribute.
        """
        if self.is_seen is True:
            return _("Seen")
        else:
            return _("Not seen")

    def is_completed(self) -> bool:
        """Checks if the assignment is completed based on the status attribute.

        If the status attribute is CON_COMPLETED, returns True. Otherwise, returns False.

        Returns:
            bool: True if the assignment is completed, False otherwise.
        """
        if self.status == CON_COMPLETED:
            return True
        else:
            return False
