from django.apps import AppConfig


class SpecialAssignmentConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "special_assignment"

    def ready(self):
        from special_assignment import cron

        cron.check_past_due_sa()
