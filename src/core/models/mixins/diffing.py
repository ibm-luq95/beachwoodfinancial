# -*- coding: utf-8 -*-#


class DiffingMixin:
    """
    A mixin class that provides functionality for tracking changes in model instances.

    This mixin class includes fields and methods that are commonly used by models to track changes in their state.

    Fields:
    - _original_state: A dictionary that stores the initial state of the model instance.

    Methods:
    - __init__(self, *args, **kwargs): Initializes the mixin by saving the initial state of the model instance.
    - get_changed_columns(self) -> dict: Returns a dictionary of columns that have changed since the model instance was created or last saved.

    """

    def __init__(self, *args, **kwargs):
        super(DiffingMixin, self).__init__(*args, **kwargs)
        self._original_state = dict(self.__dict__)

    def get_changed_columns(self) -> dict:
        """
        Returns a dictionary of columns that have changed since the model instance was
        created or last saved.

        Returns:
            dict: A dictionary with column names as keys and their original values as values.

        """
        missing = object()
        result = {}
        for key, value in self._original_state.items():
            if key != self.__dict__.get(key, missing):
                result[key] = value
        return result
