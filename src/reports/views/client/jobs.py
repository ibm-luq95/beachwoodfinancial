# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import FormView

from client.models import ClientProxy
from core.cache import BWSiteSettingsViewMixin
from core.forms.per_page_form import PerPageForm
from core.utils import get_months_abbr
from core.views.mixins import BWLoginRequiredMixin
from reports.filters.client import ClientJobsFilter


# if settings.DEBUG is True:
#     from silk.profiling.profiler import silk_profile


# @method_decorator(csrf_exempt, name="dispatch")  # TODO: check if this is needed
class JobsReportView(
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
    template_name = "reports/client/jobs/list.html"

    # paginate_by = 2

    # @silk_profile(name="View Client jobs report")
    # def get(self, request, *args, **kwargs):
    #     """Handle GET requests: instantiate a blank version of the form."""
    #     context = self.get_context_data()
    #     return self.render_to_response(self.get_context_data())

    # def get_queryset(self):
    #     form = self.get_form()
    #     page = int(self.request.GET.get("page", 1))
    #     object_list = ClientProxy.reports_manager.get_all_jobs_as_list(
    #         form.serialize_inputs(), page
    #     )
    #     debugging_print(object_list)
    #     return object_list

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = _("Clients jobs report")
        # object_list = ClientProxy.objects.order_by("name")
        # object_list = Paginator(object_list=object_list, per_page=10)
        # context.setdefault("page_obj", object_list)
        # debugging_print(form.serialize_inputs())
        page = int(self.request.GET.get("page", 1))
        per_page = int(self.request.GET.get("per_page", 15))
        per_page_form = PerPageForm(initial={"per_page": per_page})
        context.setdefault("per_page_filter_form", per_page_form)
        context.setdefault("page_header", _("Reports".title()))

        months_list = get_months_abbr(return_months_idxs=True)
        # months_list = [str(m) for m in months_list]
        context.setdefault("months_list", months_list)
        form = self.get_form()

        object_list = ClientProxy.reports_manager.get_all_jobs_as_list(
            form.serialize_inputs(), page, per_page_form.fields.get("per_page").initial
        )
        context.setdefault("object_list", object_list)
        # form["created_year"].initial = timezone.now().year
        # created_year = form.serialize_inputs().get("period_year")
        # created_year = timezone.now().year
        # DebuggingPrint.pprint(form.serialize_inputs())
        # if form.serialize_inputs().get("period_year") is not None:
        #     created_year = None
        #     year = form.serialize_inputs().get("period_year")
        #
        #     if year != _("all"):
        #         created_year = int(year)
        #
        # else:
        #     # created_year = _("All")
        #     created_year = timezone.now().year
        # context.setdefault("created_year", created_year)

        return context

    # def get_initial(self):
    #     initial = super().get_initial()
    # initial_dict = dict(self.request.GET)
    # DebuggingPrint.pprint(self.get_form().serialize_inputs())
    # initial["period_year"] = str(timezone.now().year)
    # initial.update(initial_dict)
    # DebuggingPrint.pprint(initial)
    # return initial

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # kwargs.update({"initial": dict(self.request.GET)})
        kwargs.update({"request": self.request})
        return kwargs
