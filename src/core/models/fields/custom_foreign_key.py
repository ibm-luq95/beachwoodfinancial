# -*- coding: utf-8 -*-#
from django.db import models

from core.utils import foreign_key_snake_case_plural


class CustomForeignKey(models.ForeignKey):
    """
    Contributes the CustomForeignKey field to the specified class by setting the
    related_name attribute based on the snake case plural of the class name.

    Args:
        cls: The class to which the field is being contributed.
        name (str): The name of the field being contributed.
        private_only (bool): Flag indicating if the contribution is for private access only.
        **kwargs: Additional keyword arguments for flexibility.

    Returns:
        None

    """

    def contribute_to_class(self, cls, name, private_only=False, **kwargs):
        """
        Contributes the CustomForeignKey field to the specified class by setting the
        related_name attribute based on the snake case plural of the class name.

        Args:
            cls: The class to which the field is being contributed.
            name (str): The name of the field being contributed.
            private_only (bool): Flag indicating if the contribution is for private access only.
            **kwargs: Additional keyword arguments for flexibility.

        Returns:
            None

        """
        super().contribute_to_class(cls, name, private_only=False, **kwargs)
        self.remote_field.related_name = foreign_key_snake_case_plural(cls.__name__)
