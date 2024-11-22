from django.db import models
from django.utils.translation import gettext as _


class CronColumnMixin(models.Model):
    """
    Abstract base class that adds a `updated_by_cron` field to a model.

    The `updated_by_cron` field is a boolean field that indicates whether the model was updated by a cron job.
    It is indexed for faster querying and cannot be edited directly by users.

    Attributes:
        updated_by_cron (models.BooleanField): A boolean field that indicates if the model was updated by a cron job.

    Meta:
        abstract = True: This class is meant to be used as a base class and cannot be instantiated on its own.

    """

    updated_by_cron = models.BooleanField(
        _("updated by cron"),
        default=False,
        db_index=True,
        editable=False,
        help_text=_("This will indicate if updated by cron"),
    )

    class Meta:
        abstract = True
