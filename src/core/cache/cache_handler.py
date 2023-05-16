# -*- coding: utf-8 -*-#
from typing import Any, Union, Optional

from django.core.cache import cache


class BWCacheHandler:
    """This is cache mixin, which will use with any object need to handle cache"""

    @staticmethod
    def check(key: str) -> bool:
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

    @staticmethod
    def get_item(key: str) -> Union[None, Any]:
        """
        Get cache item value based on key
        Args:
            key: str: Cache key name

        Returns:
            None: If key not exists
            Any: Any object store in the cache
        """
        # print(f"############ {BWCacheHandler.check(key)} ############")
        if BWCacheHandler.check(key):
            return cache.get(key)
        else:
            return None

    @staticmethod
    def clear() -> None:
        """
        Clear all cache data
        """
        cache.clear()

    @staticmethod
    def set_item(key: str, value: Any, timeout: Optional[int] = None) -> None:
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

    @staticmethod
    def delete_item(key: str) -> None:
        """
        Delete cache item
        Args:
            key: str: Cache key name
        Returns:
            None: If key not exists
        """
        cache.delete(key)
