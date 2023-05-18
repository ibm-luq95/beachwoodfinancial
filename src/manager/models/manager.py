# -*- coding: utf-8 -*-#
from core.models.mixins import StaffMemberMixin, BaseModelMixin


class Manager(BaseModelMixin, StaffMemberMixin):
    """Manager model represents the manager of the app

    Args:
        CustomUser (User): Django custom user model
    """

    def __str__(self) -> str:
        # return f"Assistant - {self.user.first_name} {self.user.last_name}"
        return f"{self.user.fullname}"

    class Meta:
        # proxy = True
        permissions = [
            ("manager_user", "Manager User"),
        ]
