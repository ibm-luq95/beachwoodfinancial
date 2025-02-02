from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import FormView

from core.cache import BWSiteSettingsViewMixin
from core.views.mixins import BWLoginRequiredMixin
from reports.filters.client import ClientJobsFilter
from django.utils.translation import gettext as _


class NewReportView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWSiteSettingsViewMixin,
    # BWBaseListViewMixin,
    FormView,
    # ListView,
):
    # context_object_name = "clients_object_list"
    http_method_names = ["get"]
    form_class = ClientJobsFilter
    success_url = reverse_lazy("dashboard:reports:clients_reports:job_reports_list")

    permission_required = "client.can_view_jobs_report"

    permission_denied_message = _("You do not have permission to access this page.")
    template_name = "reports/new_report.html"