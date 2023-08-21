# -*- coding: utf-8 -*-#
from typing import Any
from uuid import UUID

from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Model
from django.forms import model_to_dict


class BWCustomJSONEncoder(DjangoJSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, UUID):
            return str(o)
        elif isinstance(o, Model):
            return model_to_dict(o)
        return super().default(o)
