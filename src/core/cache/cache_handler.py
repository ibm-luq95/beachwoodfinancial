# -*- coding: utf-8 -*-#
import traceback
from typing import Any, Union, Optional
from django.utils.translation import gettext as _

from django.core.cache import cache
from django.utils.translation import gettext as _

from core.utils import colored_output_with_logging, get_formatted_logger, debugging_print

logger = get_formatted_logger("bw_error_logger")


class BWCacheHandler:
    """
    This class provides methods for handling cache operations.
    """

    @staticmethod
    def check_site_exists(
        site_domain: str, key: Optional[str] = None, is_only_site: bool = False
    ) -> Union[bool, None]:
        """
        Check if a specific cache key exists in cache for a given site domain.

        Args:
            site_domain (str): The site domain to check.
            key (Optional[str], optional): The cache key to check. Defaults to None.
            is_only_site (bool, optional): If True, only checks if the site domain exists in cache.
                If False, checks if the cache key exists in the site domain's cache dictionary.
                Defaults to False.

        Returns:
            Union[bool, None]: True if the cache key exists, False if the site domain exists but the
                cache key does not exist, and None if the site domain does not exist in cache.

        """
        # Check if the site domain exists in cache
        if cache.get(site_domain) is not None:
            # If is_only_site is True, return True if the site domain exists
            if is_only_site:
                return True
            # If is_only_site is False, check if the cache key exists in the site domain's cache dictionary
            else:
                site_cache = cache.get(site_domain)
                if key in site_cache:
                    return True
                else:
                    return False
        else:
            return None

    @staticmethod
    def get_site_dict(site_domain: str) -> Union[dict, None]:
        """
        Get the dictionary cache for a specific site in the cache.

        Args:
            site_domain (str): The domain of the site.

        Returns:
            dict: The dictionary object stored in the cache for the site.
            None: If the site domain does not exist in the cache.

        """
        # Get the cache for the site domain
        site_cache = cache.get(site_domain)

        # If the site cache exists, return it
        if site_cache is not None:
            return site_cache
        else:
            # If the site cache does not exist, return None
            return None

    @staticmethod
    def get_item(site_domain: str, key: Optional[str] = None) -> Union[Any, None]:
        """
        Get the value of a cache item based on the key for a specific site domain.

        Args:
            site_domain (str): The domain of the site.
            key (Optional[str]): The cache key name. Defaults to None.

        Returns:
            Union[Any, None]: The value of the cache item if it exists, None otherwise.

        """
        # Get the dictionary cache for the site domain
        site_cache = BWCacheHandler.get_site_dict(site_domain)

        # If the site cache exists
        if site_cache is not None:
            # If the key exists in the site cache
            if key in site_cache.keys():
                # Return the value of the cache item
                return site_cache.get(key)
            else:
                # Log an error message if the key does not exist for the site domain
                logger.error(_(f"The key {key} does not exist for site {site_domain}!"))
                return None
        else:
            # Log an error message if the site domain does not exist in the cache
            logger.error(_(f"The site {site_domain} has no values in the cache!"))
            return None

    @staticmethod
    def clear() -> None:
        """
        Clear all cache data.

        This method clears all cached data by calling the clear function of the cache
        object.

        """
        cache.clear()

    @staticmethod
    def set_item(
        site_domain: str, key: str, value: Any, timeout: Optional[int] = None
    ) -> None:
        """
        Set cache item value based on key.

        Args:
            site_domain (str): The domain of the site.
            key (str): The cache key name.
            value (Any): The value to store.
            timeout (Optional[int]): Timeout in seconds. Defaults to None.

        Raises:
            Exception: If an error occurs during the cache setting process.

        """
        try:
            # Check if the site domain exists in the cache
            check_site = BWCacheHandler.check_site_exists(site_domain)
            site_cache_dict = None  # Initialize the site cache data

            if check_site:
                # The site domain dict exists in the cache
                site_cache_dict = BWCacheHandler.get_site_dict(site_domain)
            else:
                # The site does not exist, initialize new values
                site_cache_dict = dict()

            # Update the site cache with the new key-value pair
            site_cache_dict.update({key: value})

            # Set the cache with the updated data and timeout
            cache.set(site_domain, site_cache_dict, timeout)
        except Exception as ex:
            # Log and handle the exception
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
        Delete cache item.

        Args:
            site_domain (str): The site domain.
            key (Optional[str]): The cache key name. Defaults to None.
            is_only_site (bool): If True, delete the whole site cache dict. Defaults to False.

        Returns:
            None: If key not exists.

        Raises:
            Exception: If an error occurs during the cache deletion process.

        """
        try:
            # If is_only_site is True, delete the whole site cache dict
            if is_only_site:
                cache.delete(site_domain)
            else:
                # Delete only one key in the site cache dict
                site_data = BWCacheHandler.get_site_dict(site_domain)
                if key in site_data.keys():
                    del site_data[key]
                    BWCacheHandler.set_item(site_domain, key, site_data)
                else:
                    # Log an error message if the key does not exist in the cache
                    logger.error(_(f"The key {key} not exists! Can't delete!"))
        except Exception as ex:
            # Log and handle the exception
            logger.error(str(ex))
            colored_output_with_logging(
                is_logged=True, text=str(ex), log_level="error", color="red"
            )
            raise Exception(str(ex))

    @staticmethod
    def update_item(
        site_domain: str,  # The domain of the site
        key: str,  # The cache key name
        value: Any,  # The value to store
        timeout: Optional[int] = None,  # The timeout expiration time
    ) -> None:
        """
        Update the value of a cache item based on its key.

        Args:
            site_domain (str): The domain of the site.
            key (str): The cache key name.
            value (Any): The value to store.
            timeout (Optional[int], optional): The timeout expiration time. Defaults to None.

        Returns:
            None: If the key does not exist.

        Raises:
            Exception: If an error occurs during the cache update process.

        """
        try:
            # Call the set_item method to update the cache item
            BWCacheHandler.set_item(site_domain, key, value, timeout)
        except Exception as ex:
            # Log and handle the exception
            logger.error(str(ex))
            colored_output_with_logging(
                is_logged=True, text=str(ex), log_level="error", color="red"
            )
            raise Exception(str(ex))
