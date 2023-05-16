# -*- coding: utf-8 -*-#
from decouple import config
from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site
from django.db import transaction

# import colorama
from colorama import Fore

from core.management.mixins import CommandStdOutputMixin


class Command(BaseCommand, CommandStdOutputMixin):
    help = "Initiate django site, django site framework"

    def add_arguments(self, parser):
        parser.add_argument(
            "-i",
            "--init-set-site",
            nargs="?",
            action="store",
            const=True,
            type=str,
            help="Set django site settings",
            required=False,
        )
        parser.add_argument(
            "-c",
            "--clear-current-sites",
            nargs="?",
            action="store",
            const=True,
            type=str,
            help="Clear all current site for django",
            required=False,
        )

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                # print(Fore.YELLOW)
                init_set_site = options.get("init_set_site")
                clear_current_sites = options.get("clear_current_sites")
                if clear_current_sites is True:
                    all_sites = Site.objects.all()

                    if all_sites:
                        confirm = input(
                            Fore.YELLOW + f"Do you want to delete all sites {all_sites}? "
                        )
                        if confirm == "Y" or confirm == "y":
                            self.stdout_output(
                                "warn", f"Clear all exists sites ({all_sites.count()}) ..."
                            )
                            for site in all_sites:
                                self.stdout_output("warn", f"Deleting - ({site.name})")
                                site.delete()
                        else:
                            self.stdout_output("warn", "Quiting...")
                            return
                    else:
                        self.stdout_output("warn", "No sites to delete")
                # else:
                #     self.stdout_output("error", "You have to pass -i option!")

                if init_set_site is True:
                    site_domain = config("SITE_DOMAIN", cast=str)
                    site_name = config("SITE_NAME", cast=str)
                    self.stdout_output("warn", f"Site domain - {site_domain}")
                    self.stdout_output("warn", f"Site name - {site_name}")
                    site_data = {
                        "name": site_name,
                        "domain": site_domain,
                        "defaults": {"domain": site_domain},
                    }
                    site_obj, created = Site.objects.get_or_create(**site_data)
                    if created is True:
                        self.stdout_output(
                            "success", f"Site created successfully - {site_obj}"
                        )
                    else:
                        self.stdout_output("warn", f"Site already exists - {site_obj}")

        except Exception as ex:
            self.stdout_output("error", str(ex))
