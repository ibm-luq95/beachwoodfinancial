# -*- coding: utf-8 -*-#
class DiffingMixin:
    def __init__(self, *args, **kwargs):
        super(DiffingMixin, self).__init__(*args, **kwargs)
        self._original_state = dict(self.__dict__)

    def get_changed_columns(self) -> dict:
        missing = object()
        result = {}
        for key, value in self._original_state.items():
            if key != self.__dict__.get(key, missing):
                result[key] = value
        return result
