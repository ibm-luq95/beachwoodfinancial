# -*- coding: utf-8 -*-#
import traceback
from pathlib import Path
import pandas as pd
from prettytable import PrettyTable
import numpy as np
from django.conf import settings
from django.utils.dateparse import parse_date, parse_datetime
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.translation import gettext as _

from client.models import ClientProxy
from client_account.models import ClientAccount
from core.management.mixins import CommandStdOutputMixin
from core.utils import debugging_print, PasswordHasher
from core.utils.grab_env_file import grab_env_file
from job.models import JobProxy
from special_assignment.models import SpecialAssignmentProxy
from task.models import TaskProxy


class Command(BaseCommand, CommandStdOutputMixin):
    help = _("Migrate old data from old version")

    def add_arguments(self, parser):
        parser.add_argument(
            "-a", "--apps", help=_("App to migrate"), action="append", required=False
        )
        parser.add_argument(
            "-c",
            "--clear",
            action="store_true",
            required=False,
            default=False,
            help=_("Delete all current data (RISKY)"),
        )

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                apps = options.get("apps")
                clear = options.get("clear")
                # ss = migrated_data_dir = (
                #     settings.BASE_DIR
                #     / "core"
                #     / "management"
                #     / "commands"
                #     / "migrated_data"
                #     / "CompanyService-2023-09-05.csv"
                # )
                # df = pd.read_csv(ss)
                # debugging_print(list(df.columns))
                # psd = df["password"][0]
                # old_key = "i1hUQs_Y2U_UOPMYg1T6SAbJahDrirvZLvuVxsoo71I="
                # old_key = bytes(old_key, "ascii")
                # d = PasswordHasher.decrypt(psd, old_key)
                # debugging_print(d)
                # return
                if clear is True:
                    self.stdout_output("warn", _("Clear all data permanently!"))
                    confirm = input("").lower()
                    if confirm == "y":
                        self.stdout_output("warn", _(f"Start delete tasks..."))
                        tasks_count = TaskProxy.original_objects.all().count()
                        TaskProxy.original_objects.all().delete()
                        self.stdout_output(
                            "success", _(f"All tasks {tasks_count} deleted!")
                        )
                        self.stdout_output("warn", _(f"Start delete jobs..."))
                        jobs_count = JobProxy.original_objects.all().count()
                        JobProxy.original_objects.all().delete()
                        self.stdout_output("success", _(f"All jobs {jobs_count} deleted!"))
                        self.stdout_output(
                            "warn", _(f"Start delete special assignments...")
                        )
                        special_assignments_count = (
                            SpecialAssignmentProxy.original_objects.all().count()
                        )
                        SpecialAssignmentProxy.original_objects.all().delete()
                        self.stdout_output(
                            "success",
                            _(
                                "All special assignments"
                                f" {special_assignments_count} deleted!"
                            ),
                        )
                        self.stdout_output("warn", _(f"Start delete client accounts..."))
                        client_accounts_count = (
                            ClientAccount.original_objects.all().count()
                        )
                        ClientAccount.original_objects.all().delete()
                        self.stdout_output(
                            "success",
                            _(f"All client accounts {client_accounts_count} deleted!"),
                        )
                        self.stdout_output("warn", _("Start delete clients..."))
                        clients_count = ClientProxy.original_objects.all().count()
                        ClientProxy.original_objects.all().delete()
                        self.stdout_output(
                            "success", _(f"All clients {clients_count} deleted!")
                        )

                        self.stdout_output("success", _("All data deleted!"))
                        return
                migrated_data_dir = (
                    settings.BASE_DIR
                    / "core"
                    / "management"
                    / "commands"
                    / "migrated_data"
                )

                # debugging_print(migrated_data_dir)
                if migrated_data_dir.exists() is False:
                    raise FileNotFoundError(_("Migrated old data not exists!"))
                if apps:
                    self.stdout_output("warn", _(f"First import client from admin panel!!"))
                    if "job" in apps:
                        job_pretty_table = PrettyTable()
                        job_pretty_table.field_names = [
                            "id",
                            "client",
                            "title",
                            "description",
                            "job_type",
                            "status",
                            "note",
                            "is_deleted",
                            "created_at",
                        ]
                        p_table_jobs_rows = []
                        new_jobs_list = []
                        job_file_path = migrated_data_dir / "Job-2023-09-05.csv"
                        job_df = pd.read_csv(job_file_path)
                        job_df = job_df.replace(np.nan, None)
                        job_df_cols = list(job_df.columns)
                        # TaskProxy.original_objects.all().delete()
                        # SpecialAssignmentProxy.original_objects.all().delete()
                        # JobProxy.original_objects.all().delete()
                        # return
                        # debugging_print(job_df.columns.item())
                        # debugging_print(job_df_cols)
                        # debugging_print(job_df)
                        # 'Name' and 'Age' column respectively.
                        for i in range(len(job_df)):
                            client_pk = job_df.loc[i, "client"]
                            # debugging_print(client_pk)
                            # debugging_print(job_df.loc[i])
                            client_obj = ClientProxy.objects.filter(pk=client_pk)
                            if not client_obj:
                                self.stdout_output(
                                    "warn", _(f"Client with {client_pk} not exists!")
                                )
                                client_obj = None
                            else:
                                client_obj = client_obj.first()

                            new_job_data = {
                                "id": job_df.loc[i, "id"],
                                "client": client_obj,
                                "title": job_df.loc[i, "title"],
                                "description": job_df.loc[i, "description"],
                                "job_type": job_df.loc[i, "job_type"],
                                "status": job_df.loc[i, "status"],
                                "note": job_df.loc[i, "note"],
                                "is_deleted": job_df.loc[i, "is_deleted"],
                            }
                            if job_df.loc[i, "start_date"]:
                                new_job_data.update(
                                    {"start_date": parse_date(job_df.loc[i, "start_date"])}
                                )
                            if job_df.loc[i, "created_at"]:
                                new_job_data.update(
                                    {
                                        "created_at": parse_datetime(
                                            job_df.loc[i, "created_at"]
                                        )
                                    }
                                )
                            if job_df.loc[i, "due_date"]:
                                new_job_data.update(
                                    {"due_date": parse_date(job_df.loc[i, "due_date"])}
                                )
                            if job_df.loc[i, "deleted_at"]:
                                new_job_data.update(
                                    {
                                        "deleted_at": parse_datetime(
                                            job_df.loc[i, "deleted_at"]
                                        )
                                    }
                                )
                            if job_df.loc[i, "updated_at"]:
                                new_job_data.update(
                                    {
                                        "updated_at": parse_datetime(
                                            job_df.loc[i, "updated_at"]
                                        )
                                    }
                                )
                            p_table_jobs_rows.append(
                                [
                                    new_job_data.get("id"),
                                    new_job_data.get("client"),
                                    new_job_data.get("title"),
                                    new_job_data.get("description"),
                                    new_job_data.get("job_type"),
                                    new_job_data.get("status"),
                                    new_job_data.get("note"),
                                    new_job_data.get("is_deleted"),
                                    new_job_data.get("created_at"),
                                ]
                            )
                            # debugging_print(new_job_data)
                            # debugging_print(type(parse_date(job_df.loc[i, "start_date"])))
                            new_jobs_list.append(new_job_data)
                        job_pretty_table.add_rows(p_table_jobs_rows)
                        debugging_print(job_pretty_table)
                        if new_jobs_list:
                            self.stdout_output("info", _(f"Start bulk insert jobs..."))
                            for new_job in new_jobs_list:
                                self.stdout_output(
                                    "warn", _(f"New job: {new_job.get('title')}")
                                )
                                new_job_obj = JobProxy.objects.create(**new_job)
                                self.stdout_output(
                                    "success",
                                    _(f"Job {new_job_obj.pk} created successfully!"),
                                )
                                debugging_print(
                                    "##################################################"
                                )

                        # print(job_df.loc[i, "id"], job_df.loc[i, "title"])

                    if "task" in apps:
                        new_tasks_list = []
                        task_file_path = migrated_data_dir / "Task-2023-09-05.csv"
                        task_df = pd.read_csv(task_file_path)
                        task_df = task_df.replace(np.nan, None)
                        task_df_cols = list(task_df.columns)
                        # debugging_print(task_df.columns.item())
                        # debugging_print(task_df_cols)
                        # debugging_print(task_df)
                        # 'Name' and 'Age' column respectively.
                        for i in range(len(task_df)):
                            # debugging_print(task_df.loc[i].index)
                            job_pk = task_df.loc[i, "job"]
                            job_object = JobProxy.objects.filter(pk=job_pk)
                            if not job_object:
                                self.stdout_output(
                                    "warn", _(f"Job with {job_pk} not exists!")
                                )
                                job_object = None
                            else:
                                job_object = job_object.first()
                            # debugging_print(job_object)
                            task_data_dict = {
                                "id": task_df.loc[i, "id"],
                                "job": job_object,
                                "title": task_df.loc[i, "title"],
                                "additional_notes": task_df.loc[i, "additional_notes"],
                                "task_type": task_df.loc[i, "task_type"],
                                "status": task_df.loc[i, "status"],
                                "hints": task_df.loc[i, "hints"],
                            }
                            if task_df.loc[i, "created_at"]:
                                task_data_dict.update(
                                    {
                                        "created_at": parse_datetime(
                                            task_df.loc[i, "created_at"]
                                        )
                                    }
                                )
                            if task_df.loc[i, "deleted_at"]:
                                task_data_dict.update(
                                    {
                                        "deleted_at": parse_datetime(
                                            task_df.loc[i, "deleted_at"]
                                        )
                                    }
                                )
                            if task_df.loc[i, "updated_at"]:
                                task_data_dict.update(
                                    {
                                        "updated_at": parse_datetime(
                                            task_df.loc[i, "updated_at"]
                                        )
                                    }
                                )
                            new_tasks_list.append(task_data_dict)
                        # debugging_print(new_tasks_list)
                        if new_tasks_list:
                            for task in new_tasks_list:
                                self.stdout_output(
                                    "warn", _(f"New task: {task.get('title')}")
                                )
                                task_obj = TaskProxy.objects.create(**task)
                                self.stdout_output(
                                    "success",
                                    _(f"Task {task_obj.pk} created successfully!"),
                                )
                                debugging_print(
                                    "######################################################"
                                )

                    if "assignment" in apps:
                        new_assignment_list = []
                        assignment_file_path = (
                            migrated_data_dir / "SpecialAssignment-2023-09-05.csv"
                        )
                        assignment_df = pd.read_csv(assignment_file_path)
                        assignment_df = assignment_df.replace(np.nan, None)
                        for i in range(len(assignment_df)):
                            client_pk = assignment_df.loc[i, "client"]
                            # debugging_print(client_pk)
                            # debugging_print(assignment_df.loc[i])
                            client_obj = ClientProxy.objects.filter(pk=client_pk)
                            if not client_obj:
                                self.stdout_output(
                                    "warn", _(f"Client with {client_pk} not exists!")
                                )
                                client_obj = None
                            else:
                                client_obj = client_obj.first()

                            new_assignment_data = {
                                "id": assignment_df.loc[i, "id"],
                                "client": client_obj,
                                "title": assignment_df.loc[i, "title"],
                                "body": assignment_df.loc[i, "body"],
                                "attachment": assignment_df.loc[i, "attachment"],
                                "status": assignment_df.loc[i, "status"],
                                "notes": assignment_df.loc[i, "notes"],
                                "is_deleted": assignment_df.loc[i, "is_deleted"],
                                "is_seen": assignment_df.loc[i, "is_seen"],
                            }
                            if assignment_df.loc[i, "start_date"]:
                                new_assignment_data.update(
                                    {
                                        "start_date": parse_date(
                                            assignment_df.loc[i, "start_date"]
                                        )
                                    }
                                )
                            if assignment_df.loc[i, "created_at"]:
                                new_assignment_data.update(
                                    {
                                        "created_at": parse_datetime(
                                            assignment_df.loc[i, "created_at"]
                                        )
                                    }
                                )
                            if assignment_df.loc[i, "due_date"]:
                                new_assignment_data.update(
                                    {
                                        "due_date": parse_date(
                                            assignment_df.loc[i, "due_date"]
                                        )
                                    }
                                )
                            if assignment_df.loc[i, "deleted_at"]:
                                new_assignment_data.update(
                                    {
                                        "deleted_at": parse_datetime(
                                            assignment_df.loc[i, "deleted_at"]
                                        )
                                    }
                                )
                            if assignment_df.loc[i, "updated_at"]:
                                new_assignment_data.update(
                                    {
                                        "updated_at": parse_datetime(
                                            assignment_df.loc[i, "updated_at"]
                                        )
                                    }
                                )
                            # debugging_print(new_assignment_data)
                            # debugging_print(type(parse_date(job_df.loc[i, "start_date"])))
                            new_assignment_list.append(new_assignment_data)
                        if new_assignment_list:
                            for assignment in new_assignment_list:
                                assignment_obj = SpecialAssignmentProxy.objects.create(
                                    **assignment
                                )
                                self.stdout_output(
                                    "success",
                                    _(
                                        f"Assignment {assignment_obj.pk} created"
                                        " successfully!"
                                    ),
                                )

                    if "client_account" in apps:
                        old_key = "i1hUQs_Y2U_UOPMYg1T6SAbJahDrirvZLvuVxsoo71I="
                        old_key = bytes(old_key, "ascii")
                        client_account_pretty_table = PrettyTable()
                        client_account_pretty_table.field_names = [
                            "id",
                            "client",
                            "service_name",
                            "account_name",
                            "account_url",
                            "account_email",
                            "account_password",
                            "is_deleted",
                            "created_at",
                        ]
                        p_table_client_accounts = list()
                        new_client_accounts_list = []
                        client_account_file_path = (
                            migrated_data_dir / "CompanyService-2023-09-05.csv"
                        )
                        client_account_df = pd.read_csv(client_account_file_path)
                        client_account_df = client_account_df.replace(np.nan, None)
                        for i in range(len(client_account_df)):
                            client_pk = client_account_df.loc[i, "client"]
                            client_obj = ClientProxy.objects.filter(pk=client_pk)
                            if not client_obj:
                                self.stdout_output(
                                    "warn", _(f"Client with {client_pk} not exists!")
                                )
                                client_obj = None
                            else:
                                client_obj = client_obj.first()
                            new_client_account_data = {
                                "id": client_account_df.loc[i, "id"],
                                "client": client_obj,
                                "service_name": client_account_df.loc[i, "service_name"],
                                "account_name": client_account_df.loc[i, "label"],
                                "account_url": client_account_df.loc[i, "url"],
                                "status": client_account_df.loc[i, "status"],
                                # "account_email": client_account_df.loc[
                                #     i, "account_email"
                                # ],
                                "account_username": client_account_df.loc[i, "username"],
                                "is_deleted": client_account_df.loc[i, "is_deleted"],
                                "account_password": PasswordHasher.decrypt(
                                    client_account_df.loc[i, "password"], old_key
                                ),
                            }
                            if client_account_df.loc[i, "created_at"]:
                                new_client_account_data.update(
                                    {
                                        "created_at": parse_datetime(
                                            client_account_df.loc[i, "created_at"]
                                        )
                                    }
                                )
                            if client_account_df.loc[i, "deleted_at"]:
                                new_client_account_data.update(
                                    {
                                        "deleted_at": parse_datetime(
                                            client_account_df.loc[i, "deleted_at"]
                                        )
                                    }
                                )
                            if client_account_df.loc[i, "updated_at"]:
                                new_client_account_data.update(
                                    {
                                        "updated_at": parse_datetime(
                                            client_account_df.loc[i, "updated_at"]
                                        )
                                    }
                                )
                            new_client_accounts_list.append(new_client_account_data)

                        for ca in new_client_accounts_list:
                            client_account_obj = ClientAccount.objects.create(**ca)
                            p_table_client_accounts.append(
                                [
                                    client_account_obj.id,
                                    client_account_obj.client,
                                    client_account_obj.service_name,
                                    client_account_obj.account_name,
                                    client_account_obj.account_url,
                                    client_account_obj.account_email,
                                    client_account_obj.account_password,
                                    client_account_obj.is_deleted,
                                    client_account_obj.created_at,
                                ]
                            )
                        client_account_pretty_table.add_rows(p_table_client_accounts)
                        print(client_account_pretty_table)

        except KeyboardInterrupt as kerror:
            self.stdout_output("info", _("Canceled by user."))
        except Exception as ex:
            self.stdout_output("error", traceback.format_exc())
