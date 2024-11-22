# -*- coding: utf-8 -*-#
import sys

from django.contrib.sites.models import Site
from django.core.management import CommandError
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.translation import gettext as _

from core.constants.identity import LedgerFlareIdentity
from core.constants.site_settings import SITE_SETTINGS_DB_SLUG, APP_CONFIGS_DB_SLUG
from core.management.mixins import CommandStdOutputMixin
from core.utils.developments.debugging_print_object import DebuggingPrint
from core.utils.grab_env_file import grab_env_file
from site_settings.models import SiteSettings, ApplicationConfigurations


class Command(BaseCommand, CommandStdOutputMixin):
    help = _("Fix site settings, and not use cache")

    def add_arguments(self, parser):
        parser.add_argument(
            "-i",
            "--init-settings-configs",
            nargs="?",
            action="store",
            const=True,
            type=str,
            help=_("Initialize site settings & configurations"),
            required=False,
        )

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                DebuggingPrint.pprint(f"Deleting all site settings...")
                SiteSettings.original_objects.all().delete()
                data = {
                    "slug": SITE_SETTINGS_DB_SLUG,
                    "email": LedgerFlareIdentity.email_address,
                    "name": LedgerFlareIdentity.name,
                    "url": LedgerFlareIdentity.url,
                    "title": LedgerFlareIdentity.title,
                    "og_title": LedgerFlareIdentity.og_title,
                    "manager_name": LedgerFlareIdentity.manager_name,
                    "description": LedgerFlareIdentity.description,
                    "keywords": LedgerFlareIdentity.keywords,
                    "author": LedgerFlareIdentity.authos,
                    "classification": LedgerFlareIdentity.classification,
                    "og_description": LedgerFlareIdentity.og_description,
                }
                DebuggingPrint.pprint(f"Initialize new site settings...")
                sitesettings = SiteSettings.objects.create(**data)

        except KeyboardInterrupt as kerror:
            self.stdout_output("info", _("Canceled by user."))
        except Exception as ex:
            self.stdout_output("error", str(ex))
            sys.exit(1)
