# -*- coding: utf-8 -*-#
from django.apps import apps

from django.db import models
from django.utils.translation import gettext as _

from core.constants.db import CONST_CLIENT_JOBS_REPORTS_VIEW
from core.models.mixins.get_model_instance_as_dict import GetModelInstanceAsDictMixin


class ClientJobsReportsDBView(GetModelInstanceAsDictMixin, models.Model):
    """Client jobs reports db view, this model like readonly model."""
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
    job_year = models.IntegerField(null=True, blank=True)
    job_month = models.IntegerField(null=True, blank=True)

    objects = models.Manager()

    class Meta:
        managed = False
        db_table = CONST_CLIENT_JOBS_REPORTS_VIEW
        db_table_comment = _("Client jobs reports db view.")
        verbose_name = _("Client jobs reports db view")
        verbose_name_plural = _("Client jobs reports db view")
        ordering = ["client_name"]

    def __str__(self) -> str:
        return self.client_name

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
