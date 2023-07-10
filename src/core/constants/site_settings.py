# -*- coding: utf-8 -*-#
from django.utils.text import slugify

WEB_APP_SITE_SETTINGS_KEY = "web_app_site_settings"  # this for cache
APP_CONFIGS_SETTINGS_KEY = "web_app_configs"  # this for cache
SITE_SETTINGS_DB_SLUG = slugify("web app site settings")  # this for db
APP_CONFIGS_DB_SLUG = slugify("web app configs")  # this for db
