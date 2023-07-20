# -*- coding: utf-8 -*-#

from django.contrib.sites.models import Site
from django.core.management import CommandError
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.translation import gettext as _

from core.constants.identity import BWIdentity
from core.constants.site_settings import SITE_SETTINGS_DB_SLUG, APP_CONFIGS_DB_SLUG
from core.management.mixins import CommandStdOutputMixin
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
                site_data = dict()
                # check if clear_current_settings_configs & init_settings_configs passed together
                if (
                    init_settings_configs is not None
                    and clear_current_settings_configs is not None
                ):
                    raise CommandError(_(f"You cant pass init & clear in the same time!"))
                # check if the site_domain & pick_from_env_file not passed
                if pick_from_env_file is None and site_domain is None:
                    raise CommandError(
                        _(f"You must pass -s or -e options, to determine the site!")
                    )
                # check if site_domain not passed, but pick_from_env_file is passed
                # if site_domain is None and pick_from_env_file is not None:
                #     raise CommandError(_("Site domain is required!"))

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
                site_data.update(
                    {
                        "site_domain": site_object.domain,
                        "site_name": site_object.name,
                        "site_object": site_object,
                    }
                )
                # check if clear_current_settings_configs is passed
                if clear_current_settings_configs is True:
                    self.stdout_output(
                        "warn",
                        _(
                            f"Do you want to delete all site settings and configs for {site_domain}?"
                        ),
                    )
                    confirm = str(input("> "))
                    if confirm == "y" or confirm == "Y":
                        SiteSettings.original_objects.select_related().filter(
                            site=site_data.get("site_object")
                        ).delete()
                        if verbosity > 1:
                            self.stdout_output("info", _(f"Deleting site settings..."))
                        ApplicationConfigurations.original_objects.select_related().filter(
                            site=site_data.get("site_object")
                        ).delete()
                        if verbosity > 1:
                            self.stdout_output("info", _(f"Deleting app configs..."))
                        self.stdout_output(
                            "success",
                            _(
                                "Site settings and configurations are deleted successfully!"
                            ),
                        )
                    else:
                        # self.exit_code = 0
                        # sys.exit(self.exit_code)
                        self.stdout_output("warn", "Quiting...")
                        return
                if init_settings_configs is True:
                    data = {
                        "slug": SITE_SETTINGS_DB_SLUG,
                        "email": BWIdentity.email_address,
                        "name": BWIdentity.name,
                        "url": BWIdentity.url,
                        "title": BWIdentity.title,
                        "manager_name": BWIdentity.manager_name,
                        "description": BWIdentity.description,
                    }
                    data.update({"site": site_data.get("site_object")})
                    site_settings, created = SiteSettings.objects.get_or_create(
                        slug=SITE_SETTINGS_DB_SLUG, defaults=data
                    )
                    (
                        app_configs,
                        created2,
                    ) = ApplicationConfigurations.objects.get_or_create(
                        slug=APP_CONFIGS_DB_SLUG,
                        defaults={"site": site_data.get("site_object")},
                    )
                    self.stdout_output("success", site_settings)
                    self.stdout_output("success", app_configs)
                    self.stdout_output(
                        "success",
                        _(
                            "Site Settings & Application Configurations Created Successfully!"
                        ),
                    )
        except KeyboardInterrupt as kerror:
            self.stdout_output("info", _("Canceled by user."))
        except Exception as ex:
            self.stdout_output("error", str(ex))
