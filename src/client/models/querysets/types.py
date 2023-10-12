# -*- coding: utf-8 -*-#
from datetime import date
from typing import TypedDict, NotRequired


class ClientJobsFilterTypes(TypedDict):
    clients: NotRequired[list]
    categories: NotRequired[list]
    job_categories: NotRequired[list]
    managed_by: NotRequired[list]
    created_at: NotRequired[date]
    months: NotRequired[list]
    job_stats: NotRequired[list]
    created_year: NotRequired[str]
    job_status: NotRequired[list]
    job_type: NotRequired[list]
    quick_created_at: NotRequired[str]
