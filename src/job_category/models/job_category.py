# -*- coding: utf-8 -*-#
from django.db import models
from django.utils.translation import gettext as _

from core.models.mixins import BaseModelMixin, StrModelMixin


class JobCategory(BaseModelMixin, StrModelMixin):
    name = models.CharField(_("name"), max_length=60, db_index=True)

    # class Meta(BaseModelMixin.Meta):
    #     constraints = [
    #         models.UniqueConstraint(fields=["name"], name="unique_job_category_name")
    #     ]
