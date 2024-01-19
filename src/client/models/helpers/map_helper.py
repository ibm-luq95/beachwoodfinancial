# -*- coding: utf-8 -*-#
import calendar
from collections import defaultdict
from typing import Optional
from django.utils.translation import gettext as _

import click
from django.db.models import QuerySet

from core.utils import bw_log, get_months_abbr


class ClientDetailsMap:
	ALL_YEARS: Optional[set] = None
	ALL_VIEWS_QS: Optional[QuerySet] = None
	ALL_DB_VIEWS_JOBS: Optional[QuerySet] = None

	def __init__(self, client):
		self.client = client
		self.pk = self.client.pk
		self.categories = self.client.categories.all()

	def __repr__(self):
		return f"Client: PK: {self.pk}, Name: {self.client.name}, Years: {self.ALL_YEARS}"

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
		except Exception:
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
								m_y = f"{calendar.month_abbr[job_dict.get('job_month')]}_{job_dict.get('job_year')}"
								# debugging_print(m_y)
								if job_dict.get("job_month") in months_list:
									# org_years[
									#     calendar.month_abbr[job_dict.get("job_month")]
									# ] = list()
									org_years[m_y] = job_dict
									# org_years[job_dict.get("job_month")] = job_dict
								else:
									org_years[m_y] = None
								# debugging_print(
								# "####################################################################")
								if not bool(org_years):
									print("The dictionary is empty.")
								else:
									org_years = dict(sorted(org_years.items()))
								# debugging_print(org_years)
								# debugging_print(
								# "####################################################################")
							tmp_data.update({"jobs_months": org_years})
					full_years_data_list.append(tmp_data)
				# debugging_print(full_years_data_list)
				return full_years_data_list
				# return []
			else:
				return None
		except Exception:
			bw_log().print_exception(suppress=[click], show_locals=False)

	def organize_jobs_years_months(self, is_all_years: bool = False) -> dict:
		try:
			months_list = self.organize_jobs_by_months()
			years_list = list()
			clients_dict = dict()
			if is_all_years is False:
				for item in months_list:
					clients_dict.setdefault("client", item.get("client"))
					years_dict = dict()
					if item.get("jobs_months") is not None:
						for month_name, job_dicts in item.get("jobs_months").items():
							# years_list.append(item)
							job_year = str(job_dicts.get("job_year"))
							if job_year in years_dict.keys():
								years_dict[job_year].append(job_dicts)
							else:
								years_dict[job_year] = list()
								years_dict[job_year].append(job_dicts)
						years_dict = dict(sorted(years_dict.items()))
						clients_dict.setdefault("jobs", years_dict)
				# debugging_print(clients_dict)
				return clients_dict
			else:
				# data = defaultdict(list)
				data = list()
				full_data = dict()
				for item in months_list:
					tmp_month_data = defaultdict(list)
					# debugging_print(item)
					client = item.get("client")
					client_id = item.get("id")
					jobs_months: dict = item.get("jobs_months")
					if jobs_months:
						for y_m, jobs_data in jobs_months.items():
							# debugging_print(y_m)
							# bw_log().log(y_m, jobs_data)
							tmp_month_data[jobs_data.get("job_month")].append(jobs_data)
						tmp_month_data = dict(sorted(tmp_month_data.items()))
						# debugging_print(tmp_month_data)
						for month_idx, jobs_details in tmp_month_data.items():
							# debugging_print(jobs_details)
							# debugging_print(len(jobs_details))
							merged_dict = dict()
							tmp_lst = []
							ll = [
								"id",
								"job_year",
								"job_month",
								"client_name",
								"job_not_completed_count",
								"job_in_progress_count",
								"job_past_due_count",
								"job_completed_count",
								"job_draft_count",
								"job_archived_count",
								"job_not_started_count",
							]
							for tmp_job_item in jobs_details:
								# bw_log().log(tmp_job_item)
								if tmp_job_item.get("job_month") in merged_dict.keys():
									merged_dict[tmp_job_item.get("job_month")][
										"id"
									] = tmp_job_item.get("id")
									merged_dict[tmp_job_item.get("job_month")][
										"job_month"
									] = tmp_job_item.get("job_month")
									# merged_dict[tmp_job_item.get("job_month")][
									#     "client_name"
									# ] = tmp_job_item.get("client_name")
									merged_dict[tmp_job_item.get("job_month")][
										"job_not_completed_count"
									] += tmp_job_item.get("job_not_completed_count")
									merged_dict[tmp_job_item.get("job_month")][
										"job_in_progress_count"
									] += tmp_job_item.get("job_in_progress_count")
									merged_dict[tmp_job_item.get("job_month")][
										"job_past_due_count"
									] += tmp_job_item.get("job_past_due_count")
									merged_dict[tmp_job_item.get("job_month")][
										"job_completed_count"
									] += tmp_job_item.get("job_completed_count")
									merged_dict[tmp_job_item.get("job_month")][
										"job_draft_count"
									] += tmp_job_item.get("job_draft_count")
									merged_dict[tmp_job_item.get("job_month")][
										"job_archived_count"
									] += tmp_job_item.get("job_archived_count")
									merged_dict[tmp_job_item.get("job_month")][
										"job_not_started_count"
									] += tmp_job_item.get("job_not_started_count")
								else:
									merged_dict[tmp_job_item.get("job_month")] = tmp_job_item
									merged_dict[tmp_job_item.get("job_month")].update(
										{"job_year": _("All")}
									)
							# data["jobs"].append(merged_dict)
							data.append(merged_dict)
							# debugging_print(merged_dict)
							# cpprint(data)
						# full_data.update({"client": client, "jobs": data})
						full_data["client"] = client
						full_data["jobs"] = data
				# cpprint(full_data)
				return full_data
		except Exception:
			bw_log().print_exception(suppress=[click], show_locals=False)
