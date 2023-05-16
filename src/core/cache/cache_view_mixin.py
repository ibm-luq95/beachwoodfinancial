# -*- coding: utf-8 -*-#
from typing import Any, Union, Optional

from django.core.cache import cache


class CacheViewMixin:
    """This is cache mixin, which will use with any cbv"""

    def cmx_check(self, key: str) -> bool:
        """
        This method will check if specific cache key exists in cache
        Args:
            key: str = key name

        Returns:
            bool: True value exists, False otherwise
        """
        checked = cache.get(key)
        if checked is not None:
            return True
        else:
            return False

    def cmx_get_item(self, key: str) -> Union[None, Any]:
        """
        Get cache item value based on key
        Args:
            key: str: Cache key name

        Returns:
            None: If key not exists
            Any: Any object store in the cache
        """
        # print(f"############ {self.cmx_check(key)} ############")
        if self.cmx_check(key):
            return cache.get(key)
        else:
            return None

    def cmx_clear(self) -> None:
        """
        Clear all cache data
        """
        cache.clear()

    def cmx_set_item(self, key: str, value: Any, timeout: Optional[int] = None) -> None:
        """
        Set cache item value based on key
        Args:
            key: str: Cache key name
            value: Any: The value will store
            timeout: int: timeout expire
        Returns:
            None: If key not exists
        """
        cache.set(key, value, timeout)

    def cmx_delete_item(self, key: str) -> None:
        """
        Delete cache item
        Args:
            key: str: Cache key name
        Returns:
            None: If key not exists
        """
        cache.delete(key)
