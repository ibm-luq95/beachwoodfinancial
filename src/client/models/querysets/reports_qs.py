# -*- coding: utf-8 -*-#
from typing import Optional

import click
from django.core.paginator import Paginator
from django.db import transaction
from django.db.models import Q

from client.models.helpers.map_helper import ClientDetailsMap
from client.models.querysets.types import ClientJobsFilterTypes
from core.models.querysets import BaseQuerySetMixin
from core.utils import bw_log
from core.utils.developments.debugging_print_object import BWDebuggingPrint
from reports.models import ClientJobsReportsDBView


class ClientReportsQuerySet(BaseQuerySetMixin):
    def get_all_jobs_as_list(
        self,
        filter_params: Optional[ClientJobsFilterTypes] = None,
        page: Optional[int] = None,
    ) -> dict:
        from client.models.client_proxy import ClientProxy

        with transaction.atomic():
            data_list = list()
            years_list = set()
            created_year = filter_params.get("created_year")
            clients_pks = filter_params.get("clients")
            client_categories = filter_params.get("categories")
            job_categories = filter_params.get("job_categories")
            job_status = filter_params.get("job_status")
            job_type = filter_params.get("job_type")
            job_stats = filter_params.get("job_stats")
            jobs_managed_by = filter_params.get("managed_by")
            period_year = filter_params.get("period_year")
            period_month = filter_params.get("period_month")
            # debugging_print(filter_params)
            clients_q = Q()
            if client_categories is not None:
                clients_q &= Q(categories__in=client_categories)
            if clients_pks is not None:
                clients_q &= Q(pk__in=clients_pks)
            if job_categories is not None:
                clients_q &= Q(jobs__categories__in=job_categories)
            if job_stats is not None:
                clients_q &= Q(jobs__stats__in=job_stats)
            if job_type is not None:
                clients_q &= Q(jobs__type__in=job_type)
            if job_status is not None:
                clients_q &= Q(jobs__status__in=job_status)
            if jobs_managed_by is not None:
                clients_q &= Q(jobs__managed_by__in=jobs_managed_by)
            if period_year is not None:
                clients_q &= Q(jobs__period_year__in=period_year)
            if period_month is not None:
                clients_q &= Q(jobs__period_month__in=period_month)
            # debugging_print(created_year.isdigit())

            try:
                reports = (
                    ClientJobsReportsDBView.objects.select_related()
                    .all()
                    .order_by("client_name")
                )
                # BWDebuggingPrint.log(reports)
                # for r in reports:
                #     BWDebuggingPrint.log(r)
                for r in reports:
                    years_list.add(r.job_year)
                details_dict = dict()
                # bw_log().log(years_list)
                clients = (
                    ClientProxy.objects.select_related()
                    .filter(clients_q)
                    .distinct()
                    .order_by("name")
                )
                # debugging_print(len(clients))
                # debugging_print(clients.first().jobs.all())
                details_dict.setdefault("total_rows_count", len(clients))
                page_object = Paginator(clients, 10)
                details_dict.setdefault("page_obj", page_object.get_page(page))
                # debugging_print(clients.page(1).object_list)
                for client in page_object.page(page).object_list:
                    q_objects = Q(client_id=client.pk)
                    if (
                        created_year is not None and created_year.isdigit() is True
                    ):  # it should be letter case
                        q_objects &= Q(job_year=created_year)
                    client_view_results = (
                        ClientJobsReportsDBView.objects.select_related()
                        .filter(q_objects)
                        .order_by("client_name")
                    )
                    # debugging_print(str(client_view_results.count()))
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
                # debugging_print(
                #     "######################################################################"
                # )
                # debugging_print(data_list[0].organize_jobs_by_years())
                # debugging_print(data_list[0].organize_jobs_by_months())
                # debugging_print(data_list[0].organize_jobs_years_months())

                # for kk in data_list[:5]:
                # kk.organize_jobs_years_months(is_all_years=False)
                # kk.organize_jobs_years_months(is_all_years=True)
                #     debugging_print("*************************************************")
                # # data_list[3].organize_jobs_by_months()
                # debugging_print(
                #     "######################################################################"
                # )
                # debugging_print()
                details_dict.setdefault("object_list", data_list)
                return details_dict
            except Exception as e:
                bw_log().print_exception(suppress=[click], show_locals=False)
                # colored_output_with_logging(
                #     is_logged=True,
                #     text=traceback.format_exc(),
                #     log_level="error",
                #     color="red",
                # )
