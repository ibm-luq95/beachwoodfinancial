# -*- coding: utf-8 -*-#
from django.db import models
from django.forms import model_to_dict
from django.utils.translation import gettext as _

from core.constants.db import CONST_CLIENT_JOBS_REPORTS_VIEW
from core.utils import sort_dict


class ClientJobsReportsDBView(models.Model):
    """A class representing a read-only view of client job reports in the database."""

    ID_FIELD = "client_id"

    client_id = models.UUIDField(primary_key=True, editable=False)
    client_name = models.CharField(max_length=50, null=True, blank=True)
    job_completed_count = models.IntegerField(null=True, blank=True)
    job_not_completed_count = models.IntegerField(null=True, blank=True)
    job_past_due_count = models.IntegerField(null=True, blank=True)
    job_in_progress_count = models.IntegerField(null=True, blank=True)
    job_archived_count = models.IntegerField(null=True, blank=True)
    job_not_started_count = models.IntegerField(null=True, blank=True)
    job_draft_count = models.IntegerField(null=True, blank=True)
    # job_year = models.IntegerField(null=True, blank=True)
    # job_month = models.IntegerField(null=True, blank=True)
    job_period_month = models.CharField(null=True, blank=True, max_length=2)
    job_period_year = models.CharField(null=True, blank=True, max_length=4)

    objects = models.Manager()

    class Meta:
        managed = False
        db_table = CONST_CLIENT_JOBS_REPORTS_VIEW
        db_table_comment = _("Client jobs reports db view.")
        verbose_name = _("Client jobs reports db view")
        verbose_name_plural = _("Client jobs reports db view")
        ordering = ["client_name"]

    # def job_month(self):
    #     if self.job_month is not None or self.job_month != "":
    #         return int(self.job_month)
    #     return self.job_month

    @property
    def get_instance_as_dict(self) -> dict:
        data = {
            "client_id": self.client_id,
            "client_name": self.client_name,
            "job_completed_count": int(self.job_completed_count),
            "job_not_completed_count": int(self.job_not_completed_count),
            "job_past_due_count": int(self.job_past_due_count),
            "job_in_progress_count": int(self.job_in_progress_count),
            "job_archived_count": int(self.job_archived_count),
            "job_not_started_count": int(self.job_not_started_count),
            "job_draft_count": int(self.job_draft_count),
            "job_period_month": int(self.job_period_month),
            "job_period_year": int(self.job_period_year),
        }

        return sort_dict(data)

    def __str__(self) -> str:
        return f"{self.client_name} - {self.job_period_year} of {self.job_period_month}"

    def save(self, *args, **kwargs):
        raise Exception(_("Client jobs reports db view cannot be saved."))

    def delete(self, *args, **kwargs):
        raise Exception(_("Client jobs reports db view cannot be deleted."))

    def update(self, *args, **kwargs):
        raise Exception(_("Client jobs reports db view cannot be updated."))

    # @property
    # def client(self):
    #     m = apps.get_model("client", "ClientProxy")
    #     return m.objects.get(id=self.client_id)
