# -*- coding: utf-8 -*-#
from typing import Union

from django.contrib.sites.models import Site

from core.cache import BWCacheHandler
from core.constants.site_settings import WEB_APP_SITE_SETTINGS_KEY, SITE_SETTINGS_DB_SLUG
from site_settings.models import SiteSettings


# def get_web_app_settings(request) -> Union[SiteSettings, None]:
#     # if request.user.is_authenticated:
#     site_obj = Site.objects.filter(domain=request.get_host()).first()
#     if site_obj is not None:
#         site_settings = (
#             SiteSettings.objects.select_related()
#             .filter(site=site_obj, slug=SITE_SETTINGS_DB_SLUG)
#             .first()
#         )
#         if site_settings is not None:
#             if site_settings:
#                 # print(BWCacheHandler.get_item(request.get_host(), WEB_APP_SITE_SETTINGS_KEY))
#                 return BWCacheHandler.get_item(
#                     request.get_host(), WEB_APP_SITE_SETTINGS_KEY
#                 )
#             else:
#                 return None


# def return_site_settings_context(request):
#     return {"get_web_app_settings": get_web_app_settings(request)}
