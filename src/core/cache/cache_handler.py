# -*- coding: utf-8 -*-#
import traceback
from typing import Any, Union, Optional
from django.utils.translation import gettext as _

from django.core.cache import cache
from django.utils.translation import gettext as _

from core.utils import colored_output_with_logging, get_formatted_logger, debugging_print

logger = get_formatted_logger("bw_error_logger")


class BWCacheHandler:
    """This is cache mixin, which will use with any object need to handle cache"""

    @staticmethod
    def check_site_exists(
        site_domain: str, key: Optional[str] = None, is_only_site=False
    ) -> Union[bool, None]:
        """
        This method will check if specific cache key exists in cache
        Args:
            site_domain: str = Site domain
            key: str = key name
            is_only_site: bool = This will check only site without check if the key exists in its own dict

        Returns:
            bool: True value exists, False no site domain in the cache saved
            None: Means no dict in the cache for related site_domain
        """
        if cache.get(site_domain) is not None:
            return True
        else:
            return False

    @staticmethod
    def get_site_dict(site_domain: str) -> Union[dict, None]:
        """
        Get dict cache for specific site in the cache
        Parameters
        ----------
        site_domain: str: Site domain

        Returns
        -------
            dict: doct object stored in the cache
            None: The site domain not exists in the cache
        """
        site_cache = cache.get(site_domain)
        if site_cache is not None:
            return site_cache
        else:
            return None

    @staticmethod
    def get_item(site_domain: str, key: Optional[str] = None) -> Union[Any, None]:
        """
        Get cache item value based on key
        Args:
            site_domain: str: Site domain
            key: str: Cache key name

        Returns:
            Any: Any object store in the cache
            None: The item not exists in the cache
        """
        # print(f"############ {BWCacheHandler.check(key)} ############")
        site_cache = BWCacheHandler.get_site_dict(site_domain)
        if site_cache is not None:
            if key in site_cache.keys():
                return site_cache.get(key)
            else:
                logger.error(_(f"The key {key} not exists for site {site_domain}!"))
                return None
        else:
            logger.error(_(f"The site {site_domain} has no values in the cache!"))
            return None

    @staticmethod
    def clear() -> None:
        """
        Clear all cache data
        """
        cache.clear()

    @staticmethod
    def set_item(
        site_domain: str, key: str, value: Any, timeout: Optional[int] = None
    ) -> None:
        """
        Set cache item value based on key
        Args:
            site_domain: str: Site domain
            key: str: Cache key name
            value: Any: The value will store
            timeout: int: timeout expire
        Returns:
            None: If key not exists
        """
        try:
            check_site = BWCacheHandler.check_site_exists(site_domain)
            site_cache_dict = None  # the new site cache data
            if check_site is True:
                # it means the site domain dict exists in the cache
                site_cache_dict = BWCacheHandler.get_site_dict(site_domain)
            elif check_site is False:
                # this mean the site not exists, will init the new values
                site_cache_dict = dict()  # the new site cache data

            site_cache_dict.update({key: value})

            cache.set(site_domain, site_cache_dict, timeout)
        except Exception as ex:
            logger.error(str(ex))
            colored_output_with_logging(
                is_logged=True, text=str(ex), log_level="error", color="red"
            )
            raise Exception(str(ex))

    @staticmethod
    def delete_item(
        site_domain: str, key: Optional[str] = None, is_only_site=False
    ) -> None:
        """
        Delete cache item
        Args:
            site_domain: str: Site domain
            key: str: Cache key name
            is_only_site: bool: Get whole site cache dict
        Returns:
            None: If key not exists
        """
        try:
            if is_only_site is True:
                cache.delete(site_domain)
            else:
                # delete only one key in dict
                site_data = BWCacheHandler.get_site_dict(site_domain)
                if key in site_data.keys():
                    del site_data[key]
                    BWCacheHandler.set_item(site_domain, key, site_data)
                else:
                    logger.error(_(f"The key {key} not exists!, cant delete!"))
        except Exception as ex:
            colored_output_with_logging(
                is_logged=True, text=str(ex), log_level="error", color="red"
            )

    @staticmethod
    def update_item(
        site_domain: str, key: str, value: Any, timeout: Optional[int] = None
    ) -> None:
        """
        Update cache item value based on key
        Args:
            site_domain: str: Site domain
            key: str: Cache key name
            value: Any: The value will store
            timeout: int: timeout expire
        Returns:
            None: If key not exists
        """
        try:
            BWCacheHandler.set_item(site_domain, key, value, timeout)
        except Exception as ex:
            colored_output_with_logging(
                is_logged=True, text=str(ex), log_level="error", color="red"
            )
