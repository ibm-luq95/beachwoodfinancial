# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView
from django.utils.translation import gettext as _
from calendar import month_name
from silk.profiling.profiler import silk_profile
from django.utils import timezone

from client.models import ClientProxy
from core.cache import BWCacheViewMixin
from core.constants import LIST_VIEW_PAGINATE_BY
from core.utils import debugging_print, get_months_abbr
from core.views.mixins import BWLoginRequiredMixin, BWBaseListViewMixin
from job.models import JobProxy
from reports.filters.client import ClientJobsFilter
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name="dispatch")
class JobsReportView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWCacheViewMixin,
    # BWBaseListViewMixin,
    FormView,
):
    http_method_names = ["get"]
    form_class = ClientJobsFilter
    success_url = reverse_lazy("dashboard:reports:clients_reports:job_reports_list")

    permission_required = "client.can_view_jobs_report"

    permission_denied_message = _("You do not have permission to access this page.")
    template_name = "reports/client/jobs/list.html"

    # @silk_profile(name="View Client jobs report")
    # def get(self, request, *args, **kwargs):
    #     """Handle GET requests: instantiate a blank version of the form."""
    #     context = self.get_context_data()
    #     return self.render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = _("Clients jobs report")
        object_list = ClientProxy.objects.order_by("name")
        object_list = Paginator(object_list=object_list, per_page=10)
        context.setdefault("page_obj", object_list)
        form = self.get_form()
        # debugging_print(form.serialize_inputs())
        context.setdefault("page_header", _("Reports".title()))

        months_list = get_months_abbr(year=self.request.GET.get("created_year", "All"))
        # months_list = [str(m) for m in months_list]
        context.setdefault("months_list", months_list)
        # debugging_print(list(month_name))
        object_list = ClientProxy.reports_manager.get_all_jobs_as_list(
            form.serialize_inputs()
        )
        context.setdefault("object_list", object_list)

        # debugging_print(self.filterset.form["name"])
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"initial": dict(self.request.GET)})
        kwargs.update({"request": self.request})
        return kwargs