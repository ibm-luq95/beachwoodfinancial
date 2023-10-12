# -*- coding: utf-8 -*-#
import traceback
from collections import defaultdict
from typing import Optional
import click

from django.db import transaction

from client.models.querysets.types import ClientJobsFilterTypes
from core.models.querysets import BaseQuerySetMixin
from core.utils import debugging_print, colored_output_with_logging, get_months_abbr
from core.utils.developments import bw_log, bw_custom_logger
from reports.models import ClientJobsReportsDBView


class ClientReportsQuerySet(BaseQuerySetMixin):
    def get_all_jobs_as_list(
        self, filter_params: Optional[ClientJobsFilterTypes] = None
    ) -> defaultdict:
        from client.models.client_proxy import ClientProxy

        with transaction.atomic():
            year_clients = defaultdict(set)
            data = defaultdict(list)
            data_list = list()
            months_data = defaultdict(list)
            full_data = defaultdict(defaultdict)
            months_list = get_months_abbr(return_months_idxs=True)
            years_list = set()

            try:
                reports = ClientJobsReportsDBView.objects.select_related().all()
                for r in reports:
                    years_list.add(r.job_year)
                details_dict = list()
                data2 = defaultdict(dict)
                bw_log().log(years_list)
                clients = ClientProxy.objects.select_related().all()[0:5]
                bw_log().log(clients.count())
                for client in clients:
                    client_view_results = (
                        ClientJobsReportsDBView.objects.select_related().filter(
                            client_id=client.pk
                        )
                    )
                    for year in years_list:
                        years_results = client_view_results.filter(job_year=year)
                        data2["client"] = {"object": client, "year": year}
                        for year_row in years_results:
                            data2["client"].update({"jobs": {}})
                            for month in months_list:
                                if month == year_row.job_month:
                                    data2["client"]["jobs"][month] = {
                                        "completed": year_row.job_completed_count,
                                        "job_completed_count": (
                                            year_row.job_completed_count
                                        ),
                                        "job_past_due_count": year_row.job_past_due_count,
                                        "job_archived_count": year_row.job_archived_count,
                                        "job_not_started_count": (
                                            year_row.job_not_started_count
                                        ),
                                        "job_not_completed_count": (
                                            year_row.job_not_completed_count
                                        ),
                                        "job_in_progress_count": (
                                            year_row.job_in_progress_count
                                        ),
                                    }
                                else:
                                    data2["client"]["jobs"][month] = None
                            data_list.append(data2)
                        # for result in client_view_results:
                        #     bw_log().log(result.get_instance_as_dict)
                    # bw_log().log(
                    #     "#####################################################################"
                    # )
                bw_log().log(data_list)

                return full_data
            except Exception as e:
                bw_log().print_exception(suppress=[click], show_locals=True)
                # colored_output_with_logging(
                #     is_logged=True,
                #     text=traceback.format_exc(),
                #     log_level="error",
                #     color="red",
                # )
