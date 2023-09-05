from django.apps import AppConfig


class SiteSettingsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "site_settings"

    def ready(self) -> None:
        from site_settings.signals import site_settings
