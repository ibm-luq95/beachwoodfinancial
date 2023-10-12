# -*- coding: utf-8 -*-#
from django.forms import model_to_dict

from core.utils import sort_dict


class GetModelInstanceAsDictMixin:
    @property
    def get_instance_as_dict(self) -> dict:
        data = model_to_dict(self)
        if hasattr(self, "ID_FIELD"):
            data.setdefault("id", getattr(self, self.ID_FIELD))
        else:
            data.setdefault("id", self.id)
        if hasattr(self, "created_at"):
            data.setdefault("created_at", self.created_at)
        if hasattr(self, "updated_at"):
            data.setdefault("updated_at", self.updated_at)
        return sort_dict(data)
