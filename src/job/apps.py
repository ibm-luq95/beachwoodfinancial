from django.apps import AppConfig


class JobConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "job"

    def ready(self):
        import job.signals.archive_items
        from . import cron

        cron.check_past_due_jobs()
