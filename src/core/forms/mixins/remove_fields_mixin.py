# -*- coding: utf-8 -*-#
from typing import Optional


class RemoveFieldsMixin:
    def __init__(self, removed_fields: Optional[list] = None):
        if removed_fields is not None:
            for section in removed_fields:
                self.fields.pop(section)
