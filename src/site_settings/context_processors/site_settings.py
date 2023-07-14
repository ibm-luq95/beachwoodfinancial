# -*- coding: utf-8 -*-#
from typing import Union

from core.cache import BWCacheHandler
from core.constants.site_settings import WEB_APP_SITE_SETTINGS_KEY, SITE_SETTINGS_DB_SLUG
from site_settings.models import SiteSettings


def get_web_app_settings(request) -> Union[SiteSettings, None]:
    if request.user.is_authenticated:
        site_settings = (
            SiteSettings.objects.select_related()
            .filter(slug=SITE_SETTINGS_DB_SLUG)
            .first()
        )
        # print(site_settings)
        if site_settings:
            return BWCacheHandler.get_item(WEB_APP_SITE_SETTINGS_KEY)
        else:
            return None


def return_site_settings_context(request):
    return {"get_web_app_settings": get_web_app_settings(request)}
