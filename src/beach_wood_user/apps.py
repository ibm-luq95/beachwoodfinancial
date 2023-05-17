from django.apps import AppConfig


class BeachWoodUserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "beach_wood_user"

    # def ready(self) -> None:
    #     import beach_wood_user.signals.login
    #     import beach_wood_user.signals.assign_group_to_user
