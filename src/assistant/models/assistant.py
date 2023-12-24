# -*- coding: utf-8 -*-#
from django.db import models
from django.utils.translation import gettext as _

from core.choices import AssistantTypeEnum
from core.constants.users import ASSISTANT_FULL_MANAGER_PERMISSION_SHORT_NAME
from core.models.mixins import StaffMemberMixin, BaseModelMixin
from core.models.mixins.access_proxy_models_mixin import AccessProxyModelMixin


class Assistant(BaseModelMixin, StaffMemberMixin, AccessProxyModelMixin):
    """Assistant models

    Args:
        BaseModelMixin (models.Model): Django base model mixin
    """

    assistant_type = models.CharField(
        _("assistant type"),
        max_length=15,
        choices=AssistantTypeEnum.choices,
        default=AssistantTypeEnum.ALL,
    )

    class Meta(BaseModelMixin.Meta, StaffMemberMixin.Meta):
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
