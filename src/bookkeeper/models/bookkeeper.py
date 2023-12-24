# -*- coding: utf-8 -*-#
from django.db import models

from core.models.mixins import BaseModelMixin, StaffMemberMixin
from core.models.mixins.access_proxy_models_mixin import AccessProxyModelMixin


class Bookkeeper(BaseModelMixin, StaffMemberMixin, AccessProxyModelMixin):
    """Bookkeeper model

    Args:
        BaseModelMixin (models.Model): Django base model mixin
    """

    class Meta(BaseModelMixin.Meta, StaffMemberMixin.Meta):
        permissions = [
            ("bookkeeper_user", "Bookkeeper User"),
            (
                "bookkeeper_can_delete_special_assignment",
                "Bookkeeper can delete special assignment",
            ),
        ]
