# -*- coding: utf-8 -*-#

from django.db import models
from django.utils.translation import gettext as _

from core.models.mixins import BaseModelMixin, StrModelMixin, GeneralStatusFieldMixin


class ClientCategory(BaseModelMixin, GeneralStatusFieldMixin, StrModelMixin):
    name = models.CharField(_("name"), max_length=50, db_index=True, unique=True)
