# -*- coding: utf-8 -*-#
"""
File: backup_all.py
Author: Ibrahim Luqman
Date: 11/5/24

Description: Export and backup all data in the database using custom commands using django-import-export package
"""
import argparse
import traceback
from datetime import date
from pathlib import PosixPath

from django.core.management.base import BaseCommand
from django.db import transaction
from django.core import management
from django.utils.translation import gettext as _
from rich.prompt import Confirm
import time
from rich.progress import track
from rich.progress import (
    Progress,
    TextColumn,
    BarColumn,
    TimeElapsedColumn,
    TimeRemainingColumn,
    SpinnerColumn,
)

from core.management.mixins import CommandStdOutputMixin
from core.utils.developments.debugging_print_object import DebuggingPrint
from core.utils.grab_env_file import grab_env_file
from note.management.commands import export_note
from task.management.commands import export_tasks
from beach_wood_user.management.commands import export_users
from client.management.commands import export_clients
from client_category.management.commands import export_client_category
from job.management.commands import export_jobs
from job_category.management.commands import export_job_category
from document.management.commands import export_document
from special_assignment.management.commands import export_sa
from discussion.management.commands import export_discussion
from staff_briefcase.management.commands import export_briefcase
from staff_briefcase.management.commands import export_briefcase_accounts
from staff_briefcase.management.commands import export_briefcase_notes
from staff_briefcase.management.commands import export_briefcase_documents
from site_settings.management.commands import export_site_settings


class Command(BaseCommand, CommandStdOutputMixin):
    help = _(
        "Export and backup all data in the database using custom commands using django-import-export package"
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "-y",
            "--yes",
            action=argparse.BooleanOptionalAction,
            default=False,
            help=_("No Confirmation"),
            required=False,
        )

    def run(self):
        try:
            with transaction.atomic():
                commands_list: list[dict] = [
                    {
                        "app": "beach_wood_user",
                        "command": export_users.Command(),
                        "progress_msg": _("Exporting users"),
                    },
                    {
                        "app": "note",
                        "command": export_note.Command(),
                        "progress_msg": _("Exporting notes"),
                    },
                    {
                        "app": "task",
                        "command": export_tasks.Command(),
                        "progress_msg": _("Exporting tasks"),
                    },
                    {
                        "app": "client",
                        "command": export_clients.Command(),
                        "progress_msg": _("Exporting clients"),
                    },
                    {
                        "app": "client_category",
                        "command": export_client_category.Command(),
                        "progress_msg": _("Exporting client categories"),
                    },
                    {
                        "app": "job",
                        "command": export_jobs.Command(),
                        "progress_msg": _("Exporting jobs"),
                    },
                    {
                        "app": "job_category",
                        "command": export_job_category.Command(),
                        "progress_msg": _("Exporting job categories"),
                    },
                    {
                        "app": "document",
                        "command": export_document.Command(),
                        "progress_msg": _("Exporting documents"),
                    },
                    {
                        "app": "special_assignment",
                        "command": export_sa.Command(),
                        "progress_msg": _("Exporting special assignments"),
                    },
                    {
                        "app": "discussion",
                        "command": export_discussion.Command(),
                        "progress_msg": _("Exporting discussions"),
                    },
                    {
                        "app": "staff_briefcase",
                        "command": export_briefcase.Command(),
                        "progress_msg": _("Exporting staff briefcase"),
                    },
                    {
                        "app": "staff_briefcase",
                        "command": export_briefcase_accounts.Command(),
                        "progress_msg": _("Exporting staff briefcase accounts"),
                    },
                    {
                        "app": "staff_briefcase",
                        "command": export_briefcase_notes.Command(),
                        "progress_msg": _("Exporting staff briefcase notes"),
                    },
                    {
                        "app": "staff_briefcase",
                        "command": export_briefcase_documents.Command(),
                        "progress_msg": _("Exporting staff briefcase documents"),
                    },
                    {
                        "app": "site_settings",
                        "command": export_site_settings.Command(),
                        "progress_msg": _("Exporting site setting"),
                    },
                ]
                with Progress(
                    SpinnerColumn(),
                    TextColumn("[progress.description]{task.description}"),
                    BarColumn(bar_width=110),
                    "[progress.percentage]{task.percentage:>3.0f}%",
                    TimeElapsedColumn(),
                    TimeRemainingColumn(elapsed_when_finished=True),
                ) as progress:
                    exporting_task = progress.add_task(
                        _("Exporting..."), total=len(commands_list)
                    )
                    # task2 = progress.add_task("Task 2", total=200)

                    # while not progress.finished:
                    for command in commands_list:
                        # progress.update(task2, advance=1)
                        progress.update(
                            exporting_task, description=_(f"Exporting {command['app']}")
                        )

                        management.call_command(command.get("command"))
                        progress.console.log(
                            _(f"[green]Exporting {command.get('app')} completed")
                        )
                        # progress.update(task2, advance=1)
                        progress.update(
                            exporting_task,
                            advance=1,
                            description=command.get("progress_msg"),
                        )
                        time.sleep(0.5)
        except KeyboardInterrupt:
            DebuggingPrint.print("[yellow bold]Quitting...")
            quit(1)
        except Exception as ex:
            self.stdout_output("error", traceback.format_exc())
            quit(1)

    def handle(self, *args, **options):
        try:
            if options.get("yes") is True:
                self.run()
                return
            else:
                ask = Confirm.ask("Do you want to start export? [y/n]", default=True)
                if ask is False:
                    DebuggingPrint.print("[yellow bold]Quitting...")
                    return
                else:
                    self.run()
        except KeyboardInterrupt:
            DebuggingPrint.print("[yellow bold]Quitting...")
            quit(1)
        except Exception as ex:
            self.stdout_output("error", str(ex))
            quit(1)
        else:
            today_date = date.today()
            config = grab_env_file()
            exported_folder = config("EXPORTED_FROM_CLI_DIR", cast=str)
            exported_folder_path: PosixPath = PosixPath(exported_folder) / PosixPath(
                str(today_date)
            )
            DebuggingPrint.panel(
                f"[green bold]Exported files successfully at {exported_folder_path}",
                title=_("Success"),
                # subtitle=_(f"{self.app_name}(s) exported".title()),
            )
