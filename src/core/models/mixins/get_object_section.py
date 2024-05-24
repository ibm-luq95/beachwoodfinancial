from typing import Dict

from django.db import models


class GetObjectSectionMixin(models.Model):
    """
    A mixin class that provides methods to get the object section based on the presence of
    'job', 'client', or 'task' attributes.

    This mixin class provides three methods:

    - `get_object_section()`: Returns the object section based on the presence of 'job',
      'client', or 'task' attributes. If 'job' attribute is present, returns the value of
      'job' attribute. If 'client' attribute is present, returns the value of 'client'
      attribute. If 'task' attribute is present, returns the value of 'task' attribute.

    - `get_related_objects_as_dict()`: Returns a dictionary containing the values of 'job',
      'client', and 'task' attributes if they are present. The keys of the dictionary are
      'job', 'client', and 'task', and the values are the corresponding attribute values.
      If an attribute is not present, its value in the dictionary is set to None.

    - `get_multiple_sections()`: Returns a dictionary containing the object section for
      'task', 'job', and 'client' attributes. The object section is obtained by calling
      `get_object_section()` method.

    Attributes:
        job (Any): The 'job' attribute of the model instance.
        client (Any): The 'client' attribute of the model instance.
        task (Any): The 'task' attribute of the model instance.

    Methods:
        get_object_section(): Returns the object section based on the presence of 'job',
          'client', or 'task' attributes.
        get_related_objects_as_dict(): Returns a dictionary containing the values of 'job',
          'client', and 'task' attributes if they are present.
        get_multiple_sections(): Returns a dictionary containing the object section for
          'task', 'job', and 'client' attributes.

    """

    class Meta:
        abstract = True

    def get_object_section(self):
        """
        Get the object section based on the presence of 'job', 'client', or 'task'
        attributes.

        Returns:
            The value of the 'job' attribute if it exists, otherwise the value of the 'client' attribute if it exists,
            otherwise the value of the 'task' attribute if it exists.

        """

        if hasattr(self, "job"):
            return getattr(self, "job")
        elif hasattr(self, "client"):
            return getattr(self, "client")
        elif hasattr(self, "task"):
            return getattr(self, "task")

    @property
    def get_related_objects_as_dict(self) -> dict:
        """
        Returns a dictionary containing the values of 'job', 'client', and 'task'
        attributes if they are present.

        The keys of the dictionary are 'job', 'client', and 'task', and the values are the corresponding attribute values.
        If an attribute is not present, its value in the dictionary is set to None.

        Returns:
            dict: A dictionary containing the values of 'job', 'client', and 'task' attributes.

        """
        data = {"job": None, "client": None, "task": None}
        if hasattr(self, "job"):
            data.update({"job": getattr(self, "job")})
        if hasattr(self, "client"):
            data.update({"client": getattr(self, "client")})
        if hasattr(self, "task"):
            data.update({"task": getattr(self, "task")})

        return data

    @property
    def get_multiple_sections(self) -> Dict[str, str]:
        """
        Returns a dictionary containing the object section for 'task', 'job', and 'client'
        attributes.

        Returns:
            Dict[str, str]: A dictionary containing the object section for 'task', 'job', and 'client' attributes.

        """
        return {
            "task": self.get_object_section(),
            "job": self.get_object_section(),
            "client": self.get_object_section(),
        }
