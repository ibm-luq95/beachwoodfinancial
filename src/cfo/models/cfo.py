from core.models.mixins import BaseModelMixin, StaffMemberMixin
from core.models.mixins.access_proxy_models_mixin import AccessProxyModelMixin


class CFO(BaseModelMixin, StaffMemberMixin, AccessProxyModelMixin):
    """CFO model

    Represents a CFO in the application.
    Inherits from BaseModelMixin, StaffMemberMixin, and AccessProxyModelMixin.
    Meta class defines permissions for the CFO user.
    """

    class Meta(BaseModelMixin.Meta, StaffMemberMixin.Meta):
        permissions = [
            ("cfo_user", "CFO User"),
        ]
