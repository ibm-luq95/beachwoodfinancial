# -*- coding: utf-8 -*-#

from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.translation import gettext as _

from core.management.mixins import CommandStdOutputMixin
from site_settings.models import SiteSettings, ApplicationConfigurations


class Command(BaseCommand, CommandStdOutputMixin):
    help = _("Initialize web application settings")

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                data = {
                    "slug": "web app",
                    "email": "beach_wood_financial@email.com",
                    "name": "Beach Wood Financial",
                    "url": "https://app.beachwoodfinancial.com/",
                    "title": _(
                        "Beach Wood Financial - Manage bookkeeping clients with jobs"
                    ),
                    "manager_name": "Albert Salazar",
                }
                # site_settings = SiteSettings.objects.select_related().create(**data)
                site_settings, created = SiteSettings.objects.get_or_create(
                    slug="web-app", defaults=data
                )
                app_configs, created2 = ApplicationConfigurations.objects.get_or_create(
                    slug="app-configs"
                )
                self.stdout_output("success", site_settings)
                self.stdout_output("success", app_configs)
                self.stdout_output(
                    "success",
                    _("Site Settings & Application Configurations Created Successfully!"),
                )
        except Exception as ex:
            self.stdout_output("error", str(ex))
