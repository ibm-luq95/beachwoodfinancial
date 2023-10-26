# -*- coding: utf-8 -*-#
from django.utils.translation import gettext as _

from django import template

from core.utils import debugging_print

register = template.Library()


@register.simple_tag
def extract_jobs_by_years(client_jobs_dict: dict, year: int | str) -> list | None:
    """Extract jobs by years."""
    years_months_jobs = client_jobs_dict.organize_jobs_years_months()
    if years_months_jobs is not None:
        jobs = years_months_jobs.get("jobs")
        if jobs is not None:
            if year != _("All"):
                """
                {
│   │   'client_name': 'The Idagency',
│   │   'id': UUID('5320dd6f-c3ac-4c87-a62a-2476a5b3a48d'),
│   │   'job_archived_count': 0,
│   │   'job_completed_count': 0,
│   │   'job_draft_count': 0,
│   │   'job_in_progress_count': 0,
│   │   'job_month': 1,
│   │   'job_not_completed_count': 0,
│   │   'job_not_started_count': 1,
│   │   'job_past_due_count': 0,
│   │   'job_year': 2020
│   }
                """
                # debugging_print(jobs.get(year))
                return jobs.get(year)
            else:
                print("ESSE@@@")
                return [jobs]
        else:
            return None
    else:
        return None


@register.simple_tag
def extract_months_from_jobs(jobs: list) -> list | None:
    """Extract months from jobs."""
    if jobs is not None:
        return [job.get("job_month") for job in jobs]
    else:
        return None


@register.simple_tag
def extract_job_from_month(jobs: list, month: str | int) -> dict:
    """Extract job from month."""
    for job in jobs:
        if job.get("job_month") == month:
            return job
