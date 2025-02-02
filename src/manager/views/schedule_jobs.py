from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.utils.timezone import now, timedelta, make_aware, datetime
from django.db.models import Q

from beach_wood_user.models import BWUser
from core.cache import BWSiteSettingsViewMixin
from core.utils.developments.debugging_print_object import DebuggingPrint
from core.views.mixins import BWLoginRequiredMixin, BWBaseListViewMixin
from django.utils.translation import gettext as _

from job.models import JobProxy


class JobScheduleListView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWSiteSettingsViewMixin,
    BWBaseListViewMixin,
    ListView,
):
    # context_object_name = "clients_object_list"
    http_method_names = ["get"]

    permission_required = "client.can_view_jobs_report"

    permission_denied_message = _("You do not have permission to access this page.")
    template_name = "manager/schedule_jobs_list.html"

    def get_queryset(self):
        return JobProxy.objects.all()

    def get_context_data(self, **kwargs):
        """Categorize jobs into previous, current, and next week for each user (ONLY current year)"""
        context = super().get_context_data(**kwargs)
        today = now().date()  # Get today's date (ignoring time)

        context.update({"title": _("Scheduled Jobs")})

        # Get the current year
        current_year = today.year

        # Ensure start times are at 00:00:00 and end times are at 23:59:59
        def start_of_day(date):
            return make_aware(datetime.combine(date, datetime.min.time()))

        def end_of_day(date):
            return make_aware(datetime.combine(date, datetime.max.time()))

        # Define week ranges (ONLY for the current year)
        start_of_week = start_of_day(
            today - timedelta(days=today.weekday())
        )  # Monday 00:00:00
        end_of_week = end_of_day(start_of_week + timedelta(days=6))  # Sunday 23:59:59

        start_of_prev_week = start_of_day(start_of_week - timedelta(days=7))
        end_of_prev_week = end_of_day(start_of_week - timedelta(days=1))

        start_of_next_week = start_of_day(end_of_week + timedelta(days=1))
        end_of_next_week = end_of_day(start_of_next_week + timedelta(days=6))

        # Fetch only jobs from the CURRENT YEAR
        all_jobs = JobProxy.objects.filter(due_date__year=current_year)
        all_users = BWUser.objects.all()

        # Create a dictionary for user-task categorization
        user_jobs_dict = {}

        for user in all_users:
            user_jobs = all_jobs.filter(managed_by=user)  # Get jobs for this user

            user_jobs_dict[user] = {
                "previous_week": user_jobs.filter(
                    due_date__gte=start_of_prev_week, due_date__lte=end_of_prev_week
                ),
                "current_week": user_jobs.filter(
                    due_date__gte=start_of_week, due_date__lte=end_of_week
                ),
                "next_week": user_jobs.filter(
                    due_date__gte=start_of_next_week, due_date__lte=end_of_next_week
                ),
            }

        context["user_jobs_dict"] = user_jobs_dict  # Pass dictionary to template
        # DebuggingPrint.pprint(user_jobs_dict)
        return context
