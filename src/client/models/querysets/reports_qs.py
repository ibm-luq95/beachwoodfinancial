# -*- coding: utf-8 -*-#
import traceback
from typing import Optional

from django.db import transaction
from django.forms import model_to_dict

from client.models.querysets.types import ClientJobsFilterTypes
from core.models.querysets import BaseQuerySetMixin
from core.utils import debugging_print, colored_output_with_logging
from reports.models import ClientJobsReportsDBView


class ClientReportsQuerySet(BaseQuerySetMixin):
    def get_all_jobs_as_list(
        self, filter_params: Optional[ClientJobsFilterTypes] = None
    ) -> list:
        with transaction.atomic():
            try:
                reports = ClientJobsReportsDBView.objects.filter(job_year=2020)
                for r in reports:
                    dd = model_to_dict(r)
                    #     dd.update({"id": r.client})
                    debugging_print(dd)
                return reports
            except Exception as e:
                print(traceback.format_exc())
                colored_output_with_logging(
                    is_logged=True,
                    text=traceback.format_exc(),
                    log_level="error",
                    color="red",
                )
