# -*- coding: utf-8 -*-#
from core.constants.users import ASSISTANT_FULL_MANAGER_PERMISSION_WITH_MODEL_NAME
from .assistant import Assistant


class AssistantProxy(Assistant):
    class Meta:
        proxy = True

    def is_has_manager_permissions(self) -> bool:
        # return self.user.get_all_permissions()
        return self.user.has_perm(ASSISTANT_FULL_MANAGER_PERMISSION_WITH_MODEL_NAME)
