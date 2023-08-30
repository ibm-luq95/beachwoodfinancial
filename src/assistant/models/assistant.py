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
