# -*- coding: utf-8 -*-#
from core.models.mixins import StaffMemberMixin, BaseModelMixin


class Manager(BaseModelMixin, StaffMemberMixin):
    """Manager model represents the manager of the app

    Args:
        CustomUser (User): Django custom user model
    """

    class Meta:
        # proxy = True
        permissions = [("manager_user", "Manager User")]
