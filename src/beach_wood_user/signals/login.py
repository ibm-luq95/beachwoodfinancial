# -*- coding: utf-8 -*-#
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from core.utils import debugging_print


@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    # if user.user_type == "manager":
    debugging_print("LOGIN NOW")
    # site_settings = SiteSettings.objects.select_related().filter(slug="web-app").first()
    # app_configs = ApplicationConfigurations.objects.filter(slug="app-configs").first()
    # if site_settings:
    #     BWCacheHandler.set_item(WEB_APP_SITE_SETTINGS_KEY, site_settings)
    # if app_configs:
    #     BWCacheHandler.set_item(APP_CONFIGS_SETTINGS_KEY, app_configs)
