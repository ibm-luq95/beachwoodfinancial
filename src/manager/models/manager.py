# -*- coding: utf-8 -*-#
from core.models.mixins import StaffMemberMixin, BaseModelMixin
from core.models.mixins.access_proxy_models_mixin import AccessProxyModelMixin


class Manager(BaseModelMixin, StaffMemberMixin, AccessProxyModelMixin):
    """Manager model represents the manager of the app

    Args:
        CustomUser (User): Django custom user model
    """

    class Meta(BaseModelMixin.Meta, StaffMemberMixin.Meta):
        permissions = [("manager_user", "Manager User")]
