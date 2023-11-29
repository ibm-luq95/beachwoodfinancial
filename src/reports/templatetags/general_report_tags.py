# -*- coding: utf-8 -*-#

from django import template

from client.models.helpers.map_helper import ClientDetailsMap

register = template.Library()


@register.simple_tag
def extract_jobs_by_years(
    client_jobs_dict: ClientDetailsMap, year: int | str
) -> list | dict | None:
    """Extract jobs by years."""
    is_all = False
    if year == "all":
        is_all = True
    years_months_jobs = client_jobs_dict.organize_jobs_years_months(is_all_years=is_all)
    if years_months_jobs is not None:
        jobs: dict = years_months_jobs.get("jobs")
        if jobs is not None:
            if is_all is True:
                return jobs
            else:
                return jobs.get(year)
        else:
            return None
    else:
        return None


@register.simple_tag
def extract_months_from_jobs(jobs: list | dict, year: str | int) -> list | set | None:
    """Extract months from jobs."""
    if jobs is not None:
        if year != "all":
            return [job.get("job_month") for job in jobs]
        else:
            months = []
            # debugging_print(jobs)
            for key in jobs:
                # debugging_print(type(item))
                for k, v in key.items():
                    months.append(k)

            return set(months)
    else:
        return None


@register.simple_tag
def extract_job_from_month(jobs: list, month: str | int, year: str | int) -> dict:
    """Extract job from month."""
    jobs_month = dict()
    if year != "all":
        for job in jobs:
            if job.get("job_month") == month:
                return job
    else:
        for job in jobs:
            if job.get(month) is not None:
                jobs_month = job.get(month)

    return jobs_month
