# -*- coding: utf-8 -*-#
from django.contrib.sites.models import Site
from django.core import serializers
import traceback
from collections import defaultdict
from typing import Optional
import click

from django.db import transaction
from django.db.models import QuerySet
from django.conf import settings

from client.models.querysets.types import ClientJobsFilterTypes
from core.cache import BWCacheHandler
from core.models.querysets import BaseQuerySetMixin
from core.utils import debugging_print, colored_output_with_logging, get_months_abbr
from core.utils.developments import bw_log, bw_custom_logger
from reports.models import ClientJobsReportsDBView
import calendar


class ClientDetailsMap:
    ALL_YEARS: Optional[set] = None
    ALL_VIEWS_QS: Optional[QuerySet] = None
    ALL_DB_VIEWS_JOBS: Optional[QuerySet] = None

    def __init__(self, client):
        self.client = client

    def __repr__(self):
        return f"Client: {self.client.name}, Years: {self.ALL_YEARS}"

    def organize_jobs_by_years(self) -> list | None:
        try:
            if self.ALL_VIEWS_QS is not None:
                data_list = list()

                if self.ALL_YEARS is not None:
                    years_dict = defaultdict(dict)
                    for year in self.ALL_YEARS:
                        if year not in years_dict.keys():
                            years_dict[year].update(
                                {
                                    "jobs": self.ALL_VIEWS_QS.select_related().filter(
                                        job_year=year
                                    )
                                }
                            )
                    data_list.append({"client": self.client, "years_dict": years_dict})
                    return data_list
                else:
                    return None
            else:
                return None
        except Exception as ex:
            bw_log().print_exception(suppress=[click], show_locals=True)

    def organize_jobs_by_months(self) -> list | None:
        try:
            years_jobs = self.organize_jobs_by_years()
            # debugging_print(years_jobs)
            # return []
            months_list = get_months_abbr(return_months_idxs=True)
            if years_jobs is not None:
                full_years_data_list = list()
                months_data = dict()
                for item in years_jobs:
                    tmp_data = dict()
                    client = item.get("client")
                    tmp_data.update({"client": client})
                    client_years_dict = item.get("years_dict")
                    org_years = dict()

                    for year, jobs in client_years_dict.items():
                        jobs_data = jobs.get("jobs")
                        if jobs_data:
                            # for month in months_list:
                            for job_view_row in jobs_data:
                                job_dict = job_view_row.get_instance_as_dict
                                if job_dict.get("job_month") in months_list:
                                    org_years[calendar.month_abbr[job_dict.get("job_month")]] = list()
                                    org_years[calendar.month_abbr[job_dict.get("job_month")]].append(job_dict)
                                else:
                                    org_years[calendar.month_abbr[job_dict.get("job_month")]] = None
                                tmp_data.update({"jobs_months": org_years})
                    full_years_data_list.append(tmp_data)
                debugging_print(full_years_data_list)
                return full_years_data_list
                # return []
            else:
                return None
        except Exception as ex:
            bw_log().print_exception(suppress=[click], show_locals=False)


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
                clients = ClientProxy.objects.select_related().all()
                bw_log().log(clients.count())
                for client in clients:
                    client_view_results = (
                        ClientJobsReportsDBView.objects.select_related().filter(
                            client_id=client.pk
                        )
                    )
                    client_details_map = ClientDetailsMap(client)
                    client_details_map.ALL_VIEWS_QS = client_view_results
                    years_set = set()
                    for y in client_view_results.values_list("job_year", flat=True):
                        years_set.add(y)
                    client_details_map.ALL_YEARS = years_set
                    # debugging_print(client.job_year)
                    data_list.append(client_details_map)
                    client_details_map = None
                # debugging_print(data_list)
                # for kk in data_list:
                #     debugging_print(kk.organize_jobs_by_months())
                # site_object = Site.objects.select_related().get(pk=settings.SITE_ID)
                # BWCacheHandler.set_item(
                #     site_object.domain, "clients_job_reports", data_list
                # )
                debugging_print(
                    "######################################################################"
                )
                data_list[0].organize_jobs_by_months()
                data_list[3].organize_jobs_by_months()
                debugging_print(
                    "######################################################################"
                )
                # debugging_print()
                return data_list
            except Exception as e:
                bw_log().print_exception(suppress=[click], show_locals=False)
                # colored_output_with_logging(
                #     is_logged=True,
                #     text=traceback.format_exc(),
                #     log_level="error",
                #     color="red",
                # )
