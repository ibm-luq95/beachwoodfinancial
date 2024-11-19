# -*- coding: utf-8 -*-#
from core.constants.users import (
    ASSISTANT_FULL_MANAGER_PERMISSION_WITH_MODEL_NAME,
    ASSISTANT_FULL_MANAGER_PERMISSION_SHORT_NAME,
)
from django.utils.translation import gettext as _

from .assistant import Assistant


class AssistantProxy(Assistant):
    """A proxy model for the Assistant model.

    This class acts as a proxy model for the Assistant model, allowing additional methods
    or behaviors to be defined without modifying the original Assistant model.

    Attributes:
        Inherits all attributes and behavior from the Assistant model.

    Methods:
        is_has_manager_permissions(self) -> bool:
            A method that checks if the assistant has full manager permissions.
            Returns True if the assistant has the full manager permissions, False otherwise.

    Meta:
        Contains metadata for the AssistantProxy class.
        proxy = True indicates that this is a proxy model.
    """

    class Meta(Assistant.Meta):
        proxy = True

    def is_has_manager_permissions(self) -> bool:
        """Check if the assistant has full manager permissions.

        Returns:
            bool: True if the assistant has full manager permissions, False otherwise.
        """
        return self.user.has_perm(ASSISTANT_FULL_MANAGER_PERMISSION_WITH_MODEL_NAME)
