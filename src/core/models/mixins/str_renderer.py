# -*- coding: utf-8 -*-#
import textwrap

from django.db import models

from core.constants.general import DEFAULT_SHORT_TRUNCATED_STRING


class StrModelMixin(models.Model):
    """
    A mixin class that provides a string representation for model instances.

    This mixin class provides a `__str__` method that returns a shortened version of the
    `title`, `body`, or `name` attribute of the model instance, depending on which one is
    available. If none of these attributes are available, the string representation will be
    an empty string.

    Attributes:
        title (str): The title attribute of the model instance.
        body (str): The body attribute of the model instance.
        name (str): The name attribute of the model instance.

    Methods:
        __str__(): Returns a shortened string representation of the model instance.

    """

    def __str__(self) -> str:
        if hasattr(self, "title"):
            return textwrap.shorten(
                self.title, width=DEFAULT_SHORT_TRUNCATED_STRING, placeholder="..."
            )
        elif hasattr(self, "body"):
            return textwrap.shorten(
                self.body, width=DEFAULT_SHORT_TRUNCATED_STRING, placeholder="..."
            )
        elif hasattr(self, "name"):
            return textwrap.shorten(
                self.name, width=DEFAULT_SHORT_TRUNCATED_STRING, placeholder="..."
            )
        return ""

    class Meta:
        abstract = True
