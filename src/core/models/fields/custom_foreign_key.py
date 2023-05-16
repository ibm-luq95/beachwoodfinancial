# -*- coding: utf-8 -*-#
from django.db import models

from core.utils import foreign_key_snake_case_plural


class CustomForeignKey(models.ForeignKey):
    def contribute_to_class(self, cls, name, private_only=False, **kwargs):
        super().contribute_to_class(cls, name, private_only=False, **kwargs)
        self.remote_field.related_name = foreign_key_snake_case_plural(cls.__name__)
