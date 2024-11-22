# -*- coding: utf-8 -*-#
"""
File: cache_reset.py
Author: Ibrahim Luqman
Date: 5/13/24

Description: This command will reset the data which saved in the backend cache memory
"""
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.cache import cache
from django.core.management import CommandError
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.translation import gettext as _

from core.cache import BWCacheHandler
from core.management.mixins import CommandStdOutputMixin
from core.utils import debugging_print
from core.utils.grab_env_file import grab_env_file


class Command(BaseCommand, CommandStdOutputMixin):
    help = _("Clear site cache")

    def add_arguments(self, parser):
        parser.add_argument(
            "-c",
            "--clear-site-cache",
            nargs="?",
            action="store",
            const=True,
            type=str,
            help=_("Clear site cache"),
            required=False,
        )
        parser.add_argument(
            "-ca",
            "--clear-all-sites-cache",
            nargs="?",
            action="store",
            const=True,
            type=str,
            help=_("Clear all sites cache"),
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
            "-st",
            "--set",
            nargs="?",
            action="store",
            const=True,
            type=str,
            help=_("set. (DEVELOPMENT ONLY)"),
            required=False,
        )

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                site_domain = options.get("site_domain")
                clear_site_cache = options.get("clear_site_cache")
                clear_all_sites_cache = options.get("clear_all_sites_cache")
                pick_from_env_file = options.get("pick_from_env_file")
                set_c = options.get("set")
                verbosity = options.get("verbosity")
                # check if clear_all_sites_cache
                if clear_all_sites_cache is True:
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
                    else:
                        return
                # check if pick_from_env_file passed
                if pick_from_env_file is True:
                    config = grab_env_file()
                    site_domain = config("SITE_DOMAIN", cast=str)
                else:
                    if site_domain is None:
                        raise CommandError(_("Site domain is required!"))
                    else:
                        site_domain = site_domain
                site_object = (
                    Site.objects.select_related().filter(domain=site_domain).first()
                )
                # check if site_object exists in the db
                if not site_object:
                    raise CommandError(_(f"The site domain {site_domain} not exists!"))

                # check if clear_site_cache & site_domain passed togather
                if clear_site_cache is not None and site_domain is not None:
                    self.stdout_output(
                        "warn",
                        _(f"Do you want to delete site {site_object.domain} from cache?"),
                    )
                    confirm = str(input("> ")).lower()
                    if confirm == "y":
                        BWCacheHandler.delete_item(site_object.domain, is_only_site=True)
                        self.stdout_output(
                            "success",
                            _(f"All cache deleted successfully for {site_object.domain}!"),
                        )
                        return

                # if set_c is not None:
                #     # debugging_print(BWCacheHandler.get_item(site_object.domain, is_only_site=True))
                #     BWCacheHandler.set_item(site_object.domain, "obje2c", "12345")
                #     BWCacheHandler.set_item(site_object.domain, "obje2c", "111111")
                #     debugging_print(BWCacheHandler.get_site_dict(site_object.domain))
        except KeyboardInterrupt as kerror:
            self.stdout_output("info", _("Canceled by user."))
        except Exception as ex:
            self.stdout_output("error", str(ex))
