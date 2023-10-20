# -*- coding: utf-8 -*-#
from django import template

register = template.Library()


@register.simple_tag
def extract_jobs_by_years(client_jobs_dict: dict, year: int | str) -> list | None:
    """Extract jobs by years."""
    return client_jobs_dict.get("jobs").get(year)


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
