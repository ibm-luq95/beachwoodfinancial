# -*- coding: utf-8 -*-#
from typing import Any, Union, Optional

from django.contrib.sites.models import Site
from django.core.cache import cache

from core.constants.site_settings import SITE_SETTINGS_DB_SLUG
from core.utils.developments.debugging_print_object import DebuggingPrint
from site_settings.models import SiteSettings


class BWSiteSettingsViewMixin:
    """This is cache mixin, which will use with any cbv"""

    def get_context_data(self, **kwargs):
        """
        Retrieves the context data for the view.

        This method adds additional data to the context, such as the value of `is_show_created_at`,
        the `per_page_filter_form`, and the `total_records` if applicable.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            dict: The context data for the view.

        """
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.update({"get_web_app_settings": self.get_sitesettings_cache()})
        return context

    def get_sitesettings_cache(self) -> dict | None:
        # Get the cache key from the request
        site_settings = SiteSettings.objects.select_related().filter(
            slug=SITE_SETTINGS_DB_SLUG
        )
        if site_settings:
            site_settings = site_settings.first()
            return site_settings.get_instance_as_dict
