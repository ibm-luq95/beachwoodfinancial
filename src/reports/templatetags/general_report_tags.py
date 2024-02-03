# -*- coding: utf-8 -*-#

from django import template

from client.models.helpers.map_helper import ClientDetailsMap

register = template.Library()


@register.simple_tag
def extract_job_month_idx(month_idx: str | int, job_data: dict):
	# print(locals())
	if isinstance(month_idx, int):
		month_idx = str(month_idx)
	return job_data.get(month_idx)


@register.simple_tag
def extract_jobs_by_years(
	client_jobs_dict: ClientDetailsMap, year: int | str
) -> list | dict | None:
	"""Extract jobs by years."""
	is_all = False
	# BWDebuggingPrint.log(year)
	# BWDebuggingPrint.pprint(locals())
	if year is None:
		is_all = True
	years_months_jobs = client_jobs_dict.organize_jobs_years_months(is_all_years=is_all)
	# BWDebuggingPrint.pprint(years_months_jobs)
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
	# BWDebuggingPrint.pprint(locals())
	if jobs is not None:
		if year is not None:
			return [job.get("job_period_month") for job in jobs]
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
	if year is not None:
		for job in jobs:
			if job.get("job_period_month") == month:
				return job
	else:
		for job in jobs:
			if job.get(month) is not None:
				jobs_month = job.get(month)

	return jobs_month
