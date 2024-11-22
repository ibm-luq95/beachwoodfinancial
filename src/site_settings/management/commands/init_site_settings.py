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
    help = _("Initialize web application settings and configurations")

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
        parser.add_argument(
            "-c",
            "--clear-current-settings-configs",
            nargs="?",
            action="store",
            const=True,
            type=str,
            help=_("Clear all current settings & configurations"),
            required=False,
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
            "-s",
            "--site-domain",
            action="store",
            type=str,
            help=_("Site domain which sittings & configuration related to"),
            required=False,
            nargs="?",
        )

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                site_domain = options.get("site_domain")
                init_settings_configs = options.get("init_settings_configs")
                pick_from_env_file = options.get("pick_from_env_file")
                clear_current_settings_configs = options.get(
                    "clear_current_settings_configs"
                )
                verbosity = options.get("verbosity")
                if clear_current_settings_configs is True:
                    DebuggingPrint.pprint("Clean all sites settings...")
                    SiteSettings.original_objects.all().delete()
                    DebuggingPrint.pprint("All site settings deleted successfully!")
                    return
                if init_settings_configs is True:
                    if SiteSettings.objects.filter(slug=SITE_SETTINGS_DB_SLUG).exists():
                        DebuggingPrint.print(
                            "[yellow bold] Site settings already exists in db!"
                        )
                        return
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
                        "canonical": LedgerFlareIdentity.canonical,
                    }
                    DebuggingPrint.pprint(f"Initialize new site settings...")
                    sitesettings = SiteSettings.objects.create(**data)
                    self.stdout_output("success", sitesettings)
                    self.stdout_output(
                        "success",
                        _("Site Settings Created Successfully!"),
                    )
        except KeyboardInterrupt as kerror:
            self.stdout_output("info", _("Canceled by user."))
        except Exception as ex:
            self.stdout_output("error", str(ex))
            sys.exit(1)
