from django.db import models
from django.utils.translation import gettext as _


class CronColumnMixin(models.Model):
    updated_by_cron = models.BooleanField(
        _("updated by cron"),
        default=False,
        db_index=True,
        editable=False,
        help_text=_("This will indicate if updated by cron"),
    )

    class Meta:
        abstract = True
