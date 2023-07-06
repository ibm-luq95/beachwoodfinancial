# -*- coding: utf-8 -*-#
# import colorama
import stringcase
from colorama import Fore
from decouple import Config, RepositoryEnv
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.translation import gettext as _

from core.cache import BWCacheHandler
from core.management.mixins import CommandStdOutputMixin
from core.utils import debugging_print
from site_settings.models import SiteSettings


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
                clear_current_sites = options.get("clear_current_cache_data")
                if clear_current_sites is True:
                    BWCacheHandler.clear()

                if init_set_site is True:
                    env_file_path = settings.BASE_DIR / ".env" / ".env_dev"
                    config = Config(RepositoryEnv(env_file_path))
                    site_domain = config("SITE_DOMAIN", cast=str)
                    site_name = config("SITE_NAME", cast=str)

                    # Set site in cache
                    try:
                        current_site_obj = Site.objects.get(domain=site_domain)
                        key_cache_name = stringcase.snakecase(current_site_obj.name)
                        BWCacheHandler.set_item(key_cache_name, current_site_obj)
                    except Site.DoesNotExist:
                        self.stdout_output(
                            "warn",
                            _(
                                f"Site for domain {site_domain} & name {site_name} not exists!"
                            ),
                        )

                    try:
                        site_settings = SiteSettings.objects.get(slug="web-app")
                        site_settings_key_cache = stringcase.snakecase(f"site settings web app {site_domain}")
                        BWCacheHandler.set_item(site_settings_key_cache, site_settings)
                        # app_configs = ApplicationConfigurations.objects.filter(slug="app-configs").first()

                    except SiteSettings.DoesNotExist:
                        self.stdout_output(
                            "warn",
                            _(f"The site with slug 'web-app' not exists!"),
                        )
                    debugging_print(locals())

        except Exception as ex:
            self.stdout_output("error", str(ex))
