# -*- coding: utf-8 -*-#
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.management import call_command
from django.http import HttpRequest

from core.cache import BWCacheHandler
from core.management.commands import set_site
from core.utils import get_formatted_logger

logger = get_formatted_logger()


class DynamicSiteMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request: HttpRequest):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_view(
            self, request: HttpRequest, view_func, view_args: list, view_kwargs: dict
    ):
        # This code is executed just before the view is called
        current_site = BWCacheHandler.get_item("current_site")
        # BWCacheHandler.delete_item("current_site")
        if not current_site:
            try:
                current_site_obj = Site.objects.get(domain=request.get_host())
                BWCacheHandler.set_item("current_site", current_site_obj)
            except Site.DoesNotExist:
                # current_site = Site.objects.get(id=settings.SITE_ID)
                logger.error("Site not exists")
                BWCacheHandler.set_item("current_site", None)
                logger.info("Site not exists!, will create new one...")
                call_command(set_site.Command(), init_set_site=True)

        request.site = current_site
        settings.SITE_ID = current_site.id
