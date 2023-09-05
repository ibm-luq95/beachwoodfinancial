# -*- coding: utf-8 -*-#
from core.constants.users import (
    ASSISTANT_FULL_MANAGER_PERMISSION_WITH_MODEL_NAME,
    ASSISTANT_FULL_MANAGER_PERMISSION_SHORT_NAME,
)
from django.utils.translation import gettext as _

from .assistant import Assistant


class AssistantProxy(Assistant):
    class Meta(Assistant.Meta):
        proxy = True
        permissions = [
            ("assistant_user", "Assistant User"),
            ("can_access_bookkeeper", _("Can access bookkeeper account details")),
            ("can_edit_bookkeeper", _("Can edit bookkeeper account details")),
            ("can_access_client", _("Can access client(s) account details")),
            ("can_assign_bookkeeper_to_client", _("Assign bookkeeper to client")),
            (
                ASSISTANT_FULL_MANAGER_PERMISSION_SHORT_NAME,
                "Assistant has full manager permissions",
            ),
            ("can_edit_users", "Can edit users"),
        ]

    def is_has_manager_permissions(self) -> bool:
        # return self.user.get_all_permissions()
        return self.user.has_perm(ASSISTANT_FULL_MANAGER_PERMISSION_WITH_MODEL_NAME)
