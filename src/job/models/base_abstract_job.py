from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.dateparse import parse_date
from django.utils.translation import gettext as _

from core.choices import JobStateEnum, JobStatusEnum, JobTypeEnum
from core.models.mixins import BaseModelMixin, StartAndDueDateMixin, StrModelMixin
from core.models.mixins.cron_column_mixin import CronColumnMixin
from job.models.help_messages import JOB_HELP_MESSAGES
from job_category.models import JobCategory


class BaseJobModel(BaseModelMixin, StartAndDueDateMixin, CronColumnMixin, StrModelMixin):
    managed_by = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.PROTECT,
        # related_name="jobs",
        null=True,
        blank=True,
        help_text=JOB_HELP_MESSAGES.get("managed_by"),
    )
    title = models.CharField(
        _("title"), max_length=100, null=False, help_text=JOB_HELP_MESSAGES.get("title")
    )
    description = models.TextField(
        _("description"),
        null=True,
        blank=True,
        help_text=JOB_HELP_MESSAGES.get("description"),
    )
    job_type = models.CharField(
        _("job type"),
        choices=JobTypeEnum.choices,
        # default=JobTypeEnum.NO_TYPE,
        max_length=20,
        help_text=JOB_HELP_MESSAGES.get("job_type"),
    )
    status = models.CharField(
        _("status"),
        max_length=20,
        choices=JobStatusEnum.choices,
        # default=JobStatusEnum.NOT_STARTED,
        help_text=JOB_HELP_MESSAGES.get("status"),
    )
    state = models.CharField(
        _("state"),
        max_length=20,
        choices=JobStateEnum.choices,
        default=JobStateEnum.ONGOING,
        help_text=JOB_HELP_MESSAGES.get("state"),
        null=True,
        blank=True,
    )
    categories = models.ManyToManyField(
        to=JobCategory,
        help_text=JOB_HELP_MESSAGES.get("categories"),
    )
    note = models.TextField(
        _("note"), null=True, help_text=JOB_HELP_MESSAGES.get("note"), blank=True
    )
    is_created_from_template = models.BooleanField(
        _("is created from template"),
        default=False,
        help_text=JOB_HELP_MESSAGES.get("is_created_from_template"),
        editable=False,
    )

    class Meta(BaseModelMixin.Meta):
        abstract = True

    def save(self, *args, **kwargs):
        if isinstance(self.due_date, str):
            due_date = parse_date(self.due_date)
        else:
            due_date = self.due_date
        if self.get_changed_columns().get("due_date") != due_date:
            if due_date < timezone.now().date():
                raise ValidationError(_("The date cannot be in the past!"))
        super().save(*args, **kwargs)

    def is_job_pass_due(self) -> bool:
        now = timezone.now().date()
        if self.due_date > now:
            return True
        else:
            return False

    def get_all_not_completed_tasks(self) -> tuple | None:
        if hasattr(self, "tasks"):
            filtered = filter(lambda task: task.is_completed is False, self.tasks.all())
            return tuple(filtered)
        else:
            return None
