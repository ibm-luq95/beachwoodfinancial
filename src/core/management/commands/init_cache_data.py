# -*- coding: utf-8 -*-#
"""
File: init_cache_data.py
Author: Ibrahim Luqman
Date: 5/13/24

Description: Initiate necessary data into cache, web app settings, application configurations, site
"""
import stringcase
from decouple import Config, RepositoryEnv
from django.conf import settings
from django.core import serializers
from django.contrib.sites.models import Site
from django.core.management import CommandError
from django.core.management.base import BaseCommand
from django.db import transaction
from django.forms import model_to_dict
from django.utils.translation import gettext as _

from core.cache import BWCacheHandler
from core.constants.site_settings import SITE_SETTINGS_DB_SLUG, WEB_APP_SITE_SETTINGS_KEY
from core.management.mixins import CommandStdOutputMixin
from core.utils import debugging_print
from core.utils.grab_env_file import grab_env_file
from site_settings.models import SiteSettings, ApplicationConfigurations
from site_settings.serializers import SiteSettingsSerializer


class Command(BaseCommand, CommandStdOutputMixin):
    help = _(
        "Initiate necessary data into cache, web app settings, application configurations, site"
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "-i",
            "--init-cache",
            nargs="?",
            action="store",
            const=True,
            type=str,
            help=_("Initialize data into cache"),
            required=False,
        )
        parser.add_argument(
            "-s",
            "--site-domain",
            action="store",
            type=str,
            help=_("Site domain which clear from the cache"),
            required=False,
            nargs="?",
        )
        parser.add_argument(
            "-e",
            "--pick-from-env-file",
            nargs="?",
            action="store",
            const=True,
            type=str,
            help=_("Pick site domain and name from current .env file. (DEVELOPMENT ONLY)"),
            required=False,
        )
        parser.add_argument(
            "-c",
            "--clear-current-cache-data",
            nargs="?",
            action="store",
            const=True,
            type=str,
            help=_("Clear all current data in cache"),
            required=False,
        )

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                # print(Fore.YELLOW)
                init_set_site = options.get("init_cache")
                pick_from_env_file = options.get("pick_from_env_file")
                site_domain = options.get("site_domain")
                clear_current_sites = options.get("clear_current_cache_data")
                if clear_current_sites is True:
                    self.stdout_output(
                        "warn",
                        _(f"Do you want to delete all sites saved in the cache?"),
                    )
                    confirm = str(input("> "))
                    if confirm == "y" or confirm == "Y":
                        BWCacheHandler.clear()
                        self.stdout_output(
                            "success", _(f"All cache deleted successfully!")
                        )
                    return
                # debugging_print(locals())
                # debugging_print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                # check if pick_from_env_file passed
                if pick_from_env_file is True:
                    config = grab_env_file(".env")
                    site_domain = config("SITE_DOMAIN", cast=str)
                else:
                    if site_domain is None:
                        raise CommandError(_("Site domain is required!"))
                    else:
                        site_domain = site_domain

                try:
                    site_object = Site.objects.select_related().get(domain=site_domain)
                except Site.DoesNotExist:
                    raise CommandError(_(f"The site domain {site_domain} not exists!"))
                # debugging_print(locals())
                # debugging_print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                if init_set_site is True:
                    self.stdout_output(
                        "warn", _(f"Init cache for {site_object.domain}...")
                    )

                    # Set site in cache
                    BWCacheHandler.set_item(
                        site_object.domain,
                        "site",
                        model_to_dict(site_object),
                    )

                    try:
                        site_settings = SiteSettings.objects.get(site=site_object)
                        site_settings_serializer = SiteSettingsSerializer(
                            instance=site_settings
                        )
                        # debugging_print(site_settings_serializer.data)
                        BWCacheHandler.set_item(
                            site_object.domain,
                            WEB_APP_SITE_SETTINGS_KEY,
                            site_settings_serializer.data,
                        )
                        # app_configs = ApplicationConfigurations.objects.filter(slug="app-configs").first()
                        self.stdout_output(
                            "success",
                            _(
                                f"Site settings for {site_object.domain} saved in the cache!"
                            ),
                        )

                    except SiteSettings.DoesNotExist:
                        raise CommandError(
                            _(f"The site with slug '{SITE_SETTINGS_DB_SLUG}' not exists!")
                        )

        except Exception as ex:
            self.stdout_output("error", str(ex))
