# -*- coding: utf-8 -*-#
from django.utils.translation import gettext as _

JOB_HELP_MESSAGES = {
    "bookkeeper": _("Bookkeeper of the job"),
    "assistant": _("Assistant(s) of the job"),
    "title": _("Job Title"),
    "note": _("Note(s) for this job (optional)"),
    "job_type": _("Type of this job, Recurring, Weekly, Urgent,..etc"),
    "status": _("Status of this job, Not Started, In Progress, Done,..etc"),
    "client": _("Client this job belong to"),
    "tasks": _("Tasks of this job"),
    "description": _("Description of the job"),
    "due_date": _("Due date for this job"),
    "managed_by": _("Staff member who will handle the job"),
    "state": _("Job state"),
}
