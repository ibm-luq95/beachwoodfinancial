# -*- coding: utf-8 -*-#

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext as _

from client.models import ClientProxy
from core.choices import JobStateEnum
from core.choices import JobStatusEnum
from core.choices import JobTypeEnum
from core.choices.fiscal_year import FiscalYearEnum
from core.choices.months import MonthChoices
from core.models.mixins import BaseModelMixin
from core.models.mixins import StartAndDueDateMixin
from core.models.mixins import StrModelMixin
from core.models.mixins.access_proxy_models_mixin import AccessProxyModelMixin
from core.models.mixins.cron_column_mixin import CronColumnMixin
from core.models.mixins.validate_due_date import ValidateDueDateMixin
from job_category.models import JobCategory
# from task.models import Task
from .help_messages import JOB_HELP_MESSAGES


class Job(
    ValidateDueDateMixin,
    BaseModelMixin,
    StartAndDueDateMixin,
    AccessProxyModelMixin,
    CronColumnMixin,
    StrModelMixin,
):
    """This is the job for every bookkeeper and assistant

    Args:
        BaseModelMixin (models.Model): Django model base mixin
    """

    client = models.ForeignKey(
        to=ClientProxy,
        on_delete=models.PROTECT,  # TODO: check if this should be null not protected
        null=True,
        blank=True,
        related_name="jobs",
        help_text=JOB_HELP_MESSAGES.get("client"),
    )
    managed_by = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        related_name="jobs",
        null=True,
        blank=True,
        help_text=JOB_HELP_MESSAGES.get("managed_by"),
    )
    title = models.CharField(
        _("title"), max_length=100, null=False, help_text=JOB_HELP_MESSAGES.get("title")
    )
    slug = models.SlugField(
        _("slug"), max_length=250, null=True, blank=True, editable=False
    )
    period_year = models.CharField(
        _("period year"),
        max_length=4,
        null=True,
        blank=True,
        db_index=True,
        choices=FiscalYearEnum.choices,
        help_text=JOB_HELP_MESSAGES.get("period_year"),
    )
    period_month = models.CharField(
        _("period month"),
        max_length=2,
        null=True,
        blank=True,
        db_index=True,
        choices=MonthChoices.choices,
        help_text=JOB_HELP_MESSAGES.get("period_month"),
    )
    # description = models.TextField(
    #     _("description"),
    #     null=True,
    #     blank=True,
    #     help_text=JOB_HELP_MESSAGES.get("description"),
    # )
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
        db_index=True,
    )
    status = models.CharField(
        _("status"),
        max_length=20,
        choices=JobStatusEnum.choices,
        # default=JobStatusEnum.NOT_STARTED,
        help_text=JOB_HELP_MESSAGES.get("status"),
        db_index=True,
    )
    state = models.CharField(
        _("state"),
        max_length=20,
        choices=JobStateEnum.choices,
        default=JobStateEnum.ONGOING,
        help_text=JOB_HELP_MESSAGES.get("state"),
        null=True,
        blank=True,
        db_index=True,
    )
    categories = models.ManyToManyField(
        to=JobCategory,
        related_name="jobs",
        blank=True,
        help_text=JOB_HELP_MESSAGES.get("categories"),
        db_index=True,
    )

    # tasks = models.ManyToManyField(to=Task, help_text=JOB_HELP_MESSAGES.get("tasks"))
    note = models.TextField(
        _("note"), null=True, help_text=JOB_HELP_MESSAGES.get("note"), blank=True
    )
    is_created_from_template = models.BooleanField(
        _("is_created_from_template"), default=False, editable=False
    )

    # objects = Manager()

    # not_filtered_objects = JobManager()
    # objects = JobManager()

    class Meta(BaseModelMixin.Meta):
        ordering = ["title"]
        permissions = BaseModelMixin.Meta.permissions + [
            ("list_abstract_job_template", "List abstract job template")
        ]

    # def get_absolute_url(self):
    #     return reverse("manager:jobs:details", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)

    def get_all_not_completed_tasks(self):
        filtered = filter(lambda task: task.is_completed is False, self.tasks.all())
        return tuple(filtered)

    def is_job_pass_due(self) -> bool:
        now = timezone.now().date()
        if self.due_date > now:
            return True
        else:
            return False

    def get_absolute_url(self):
        reverse_lazy("dashboard:job:details", kwargs={"pk": self.pk})

    # def get_all_assigned_users(self) -> list:
    #     all_users = []
    #     if self.bookkeeper.all():
    #         for bookkeeper in self.bookkeeper.all():
    #             all_users.append(bookkeeper)
    #
    #     if self.assistants.all():
    #         for assistant in self.assistants.all():
    #             all_users.append(assistant)
    #     return all_users
