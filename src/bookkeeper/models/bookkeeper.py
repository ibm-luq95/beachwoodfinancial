# -*- coding: utf-8 -*-#
from django.db import models

from core.models.mixins import BaseModelMixin, StaffMemberMixin


class Bookkeeper(BaseModelMixin, StaffMemberMixin):
    """Bookkeeper model

    Args:
        BaseModelMixin (models.Model): Django base model mixin
    """

    pass
