from collections import defaultdict

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import QuerySet
from django.utils import timezone
import calendar
from django.utils.translation import gettext as _
from django.views.generic import TemplateView

from bookkeeper.models import BookkeeperProxy
from client.models import Client
from core.cache import BWSiteSettingsViewMixin
from core.choices import JobStatusEnum
from core.utils.developments.debugging_print_object import DebuggingPrint
from core.views.mixins import BWLoginRequiredMixin


class NewReportView(
    # PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWSiteSettingsViewMixin,
    # BWBaseListViewMixin,
    TemplateView,
    # ListView,
):
    http_method_names = ["get"]

    permission_denied_message = _("You do not have permission to access this page.")
    template_name = "reports/new_report.html"

    def get_jobs_for_calendar(
        self, year, month, client_id="71e6ded5-eebc-45c0-a4bc-7296333bbd00"
    ):
        """
        Fetches jobs for a specific client, filtered by month and year, including bookkeepers.

        Args:
            client_id (int): The ID of the client to retrieve jobs for.
            year (str): The fiscal year to filter jobs by.
            month (str): The fiscal month to filter jobs by.

        Returns:
            dict: A dictionary where keys are days of the month, and values are lists of job details, including bookkeepers.
        """

        # Fetch the client instance with related jobs and bookkeepers
        try:
            client = Client.objects.prefetch_related("jobs", "bookkeepers").get(
                id=client_id, is_active=True
            )
        except Client.DoesNotExist:
            return {}  # Return an empty dictionary if the client is not found

        # Get all jobs associated with the client and apply filtering
        jobs = client.jobs.filter(
            is_scheduled=True, period_year=str(year), period_month=str(month)
        ).exclude(status__in=[JobStatusEnum.COMPLETED, JobStatusEnum.CANCELED])

        # Extract bookkeepers assigned to the client
        bookkeepers = client.bookkeepers.all()
        bookkeeper_list = [
            {"id": bk.id, "name": bk.name, "email": bk.email} for bk in bookkeepers
        ]

        # Dictionary to group jobs by day
        jobs_by_day = defaultdict(list)

        for job in jobs:
            day = int(job.start_date.day)  # Ensure `start_date` exists on the Job model
            jobs_by_day[day].append(
                {
                    "description": job.title,
                    # Use `title` as description for frontend compatibility
                    "status": job.status.lower(),
                    # Convert status to lowercase for JS consistency
                    "bookkeepers": bookkeeper_list,
                    # Include bookkeepers responsible for the job
                }
            )

        return dict(jobs_by_day)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        bookkeeper: QuerySet[BookkeeperProxy] = BookkeeperProxy.objects.filter(
            user__email="ian@beachwoodfinancial.com"
        ).first()
        DebuggingPrint.pprint(bookkeeper)
        context.setdefault("title", _("New Report"))
        this_month = timezone.now()
        context.setdefault("current_month", calendar.month_name[this_month.month])
        context.setdefault("current_year", this_month.year)
        context.setdefault("bookkeeper", bookkeeper)
        # DebuggingPrint.pprint(this_month)
        # DebuggingPrint.pprint(calendar.month_name[this_month.month])
        DebuggingPrint.pprint(bookkeeper.user.jobs.all())
        DebuggingPrint.pprint(bookkeeper.user.jobs.all().count())
        return context
