# -*- coding: utf-8 -*-#
from typing import Any
from uuid import UUID

from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Model
from django.forms import model_to_dict


class BWCustomJSONEncoder(DjangoJSONEncoder):
    """
    Custom JSON encoder that extends DjangoJSONEncoder.

    Overrides the default method to handle UUID and Django Model instances.

    Parameters:
    o (Any): The object to encode.

    Returns:
    Any: The encoded object.

    """

    def default(self, o: Any) -> Any:
        """
        A method that encodes objects to JSON format. Handles UUID and Django Model
        instances.

        Parameters:
            o (Any): The object to encode.

        Returns:
            Any: The encoded object.

        """
        if isinstance(o, UUID):
            return str(o)
        elif isinstance(o, Model):
            return model_to_dict(o)
        return super().default(o)
