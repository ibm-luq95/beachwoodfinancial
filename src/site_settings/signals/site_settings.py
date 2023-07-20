# -*- coding: utf-8 -*-#
from django.db.models.signals import post_save
from django.core.signals import request_started

from core.cache import BWCacheHandler
from core.utils import debugging_print, get_formatted_logger
from site_settings.models import SiteSettings
from core.constants.site_settings import WEB_APP_SITE_SETTINGS_KEY, SITE_SETTINGS_DB_SLUG
from site_settings.serializers import SiteSettingsSerializer

logger = get_formatted_logger()


def update_site_settings_cache(sender, instance, created, **kwargs):
    site_settings_object = instance
    # debugging_print(locals())
    site_settings_serializer = SiteSettingsSerializer(instance=site_settings_object)
    debugging_print(BWCacheHandler.get_site_dict(site_settings_object.site.domain))
    BWCacheHandler.update_item(
        site_settings_object.site.domain,
        WEB_APP_SITE_SETTINGS_KEY,
        site_settings_serializer.data,
    )
    debugging_print(BWCacheHandler.get_site_dict(site_settings_object.site.domain))
    # check it is not created
    # if not created:
    #     if slug == SITE_SETTINGS_DB_SLUG:
    #         BWCacheHandler.update_item(WEB_APP_SITE_SETTINGS_KEY, site_settings_object)


post_save.connect(update_site_settings_cache, SiteSettings)

# def init_cache_when_start(sender, environ, **kwargs):
#     # Your code here
#     # debugging_print(locals())
#     site_settings_cache = BWCacheHandler.get_item(WEB_APP_SITE_SETTINGS_KEY)
#     if site_settings_cache is None:
#         # debugging_print(site_settings_cache)
#         site_settings = SiteSettings.objects.filter(slug=SITE_SETTINGS_DB_SLUG).first()
#         if site_settings is None:
#             logger.warning(f"No site settings in the DB!")
#         else:
#             BWCacheHandler.set_item(WEB_APP_SITE_SETTINGS_KEY, site_settings)


# request_started.connect(init_cache_when_start)
