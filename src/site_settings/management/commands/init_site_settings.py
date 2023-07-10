# -*- coding: utf-8 -*-#
from decouple import Config, RepositoryEnv
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.translation import gettext as _

from core.constants.identity import BWIdentity
from core.constants.site_settings import SITE_SETTINGS_DB_SLUG, APP_CONFIGS_DB_SLUG
from core.management.mixins import CommandStdOutputMixin
from site_settings.models import SiteSettings, ApplicationConfigurations


class Command(BaseCommand, CommandStdOutputMixin):
    help = _("Initialize web application settings")

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                data = {
                    "slug": SITE_SETTINGS_DB_SLUG,
                    "email": BWIdentity.email_address,
                    "name": BWIdentity.name,
                    "url": BWIdentity.url,
                    "title": BWIdentity.title,
                    "manager_name": BWIdentity.manager_name,
                    "description": BWIdentity.description
                }
                env_file_path = settings.BASE_DIR / ".env" / ".env_dev"
                config = Config(RepositoryEnv(env_file_path))
                site_domain = config("SITE_DOMAIN", cast=str)
                site_name = config("SITE_NAME", cast=str)
                site = Site.objects.get(domain=site_domain)
                data.update({"site": site})
                # site_settings = SiteSettings.objects.select_related().create(**data)
                site_settings, created = SiteSettings.objects.get_or_create(
                    slug=SITE_SETTINGS_DB_SLUG, defaults=data
                )
                app_configs, created2 = ApplicationConfigurations.objects.get_or_create(
                    slug=APP_CONFIGS_DB_SLUG
                )
                self.stdout_output("success", site_settings)
                self.stdout_output("success", app_configs)
                self.stdout_output(
                    "success",
                    _("Site Settings & Application Configurations Created Successfully!"),
                )
        except Exception as ex:
            self.stdout_output("error", str(ex))
