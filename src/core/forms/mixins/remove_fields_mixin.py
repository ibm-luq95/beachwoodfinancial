# -*- coding: utf-8 -*-#
from typing import Optional, List


class RemoveFieldsMixin:
    """
    A mixin class that provides functionality to remove fields from a form.
    """

    def __init__(self, removed_fields: Optional[List[str]] = None) -> None:
        """
        Initializes the RemoveFieldsMixin instance.

        Args:
            removed_fields: A list of field names to be removed from the form. Defaults to None.

        """
        if removed_fields is not None:
            for section in removed_fields:
                self.fields.pop(section)
