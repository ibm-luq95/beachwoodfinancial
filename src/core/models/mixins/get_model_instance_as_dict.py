# -*- coding: utf-8 -*-#
from django.forms import model_to_dict

from core.utils import sort_dict


class GetModelInstanceAsDictMixin:
    """
    A mixin class that provides functionality for converting model instances to
    dictionaries.

    This mixin class includes a property that returns a dictionary representation of a model instance,
    including its attributes and their values. The dictionary is sorted alphabetically.

    Properties:
    - get_instance_as_dict: A property that returns a dictionary representation of the model instance.

    """

    @property
    def get_instance_as_dict(self) -> dict:
        """
        Returns a dictionary representation of the model instance.

        This property converts the model instance to a dictionary, including its attributes and their values.
        The dictionary is sorted alphabetically.

        Returns:
            dict: A dictionary representation of the model instance.

        """
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
