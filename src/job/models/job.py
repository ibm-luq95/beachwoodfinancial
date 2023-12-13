# -*- coding: utf-8 -*-#
from django.db import models

from client.models import ClientProxy
from .base_abstract_job import BaseJobModel
from .help_messages import JOB_HELP_MESSAGES


class Job(BaseJobModel):
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

    class Meta:
        # permissions = BaseModelMixin.Meta.permissions + [
        #     ("list_abstract_job_template", "List abstract job template")
        # ]
        indexes = [
            models.Index(name="job_client_idx", fields=["client"]),
            models.Index(name="job_title_idx", fields=["title"]),
            models.Index(name="job_type_idx", fields=["job_type"]),
            models.Index(name="job_status_idx", fields=["status"]),
            models.Index(name="job_state_idx", fields=["state"]),
            models.Index(name="job_due_date_idx", fields=["due_date"]),
            models.Index(name="job_managed_by_idx", fields=["managed_by"]),
            models.Index(name="job_start_date_idx", fields=["start_date"]),
            models.Index(
                name="created_from_template_idx",
                fields=["is_created_from_template"],
            ),
            models.Index(name="job_description_idx", fields=["description"]),
        ]

    # def get_absolute_url(self):
    #     return reverse("manager:jobs:details", kwargs={"pk": self.pk})

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
