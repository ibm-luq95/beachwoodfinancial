from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from core.cache import BWCacheViewMixin
from core.choices import JobStatusEnum, JobStateEnum
from core.config.forms import BWFormRenderer
from core.constants import LIST_VIEW_PAGINATE_BY
from core.constants.css_classes import BW_INFO_MODAL_CSS_CLASSES
from core.constants.status_labels import CON_DRAFT, CON_COMPLETED, CON_ARCHIVED
from core.constants.users import CON_BOOKKEEPER
from core.views.mixins import BWLoginRequiredMixin, BWBaseListViewMixin
from core.views.mixins.update_previous_mixin import UpdateReturnPreviousMixin
from discussion.forms import DiscussionMiniForm
from document.forms import DocumentForm
from job.filters import JobFilter
from job.forms import JobForm
from job.models import JobProxy
from note.forms import NoteForm
from special_assignment.forms import MiniSpecialAssignmentForm
from task.forms import TaskForm
from task.models import TaskProxy


class JobListView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWCacheViewMixin,
    BWBaseListViewMixin,
    ListView,
):
    permission_required = "job.can_view_list"

    permission_denied_message = _("You do not have permission to access this page.")
    template_name = "core/crudl/list.html"
    model = JobProxy

    paginate_by = LIST_VIEW_PAGINATE_BY
    list_type = "list"

    # def paginate_queryset(self, queryset, page_size):
    #     queryset = JobProxy.objects.filter(
    #         ~Q(status__in=[CON_ARCHIVED, CON_COMPLETED, CON_DRAFT])
    #     ).order_by("created_at")
    #     return super().paginate_queryset(queryset, page_size)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = _("Jobs")
        context.setdefault("filter_form", self.filterset.form)
        context.setdefault("list_type", self.list_type)
        context.setdefault("component_path", "bw_components/job/table_list.html")
        context.setdefault("page_header", _("jobs".title()))
        context.setdefault("subtitle", _("Jobs for clients".capitalize()))
        context.setdefault("actions_base_url", "dashboard:job")
        context.setdefault("filter_cancel_url", "dashboard:job:list")
        context.setdefault("table_header_title", _("C"))
        context.setdefault("table_header_subtitle", _("Jobs subtitle"))
        context.setdefault("is_show_create_btn", True)
        context.setdefault("pagination_list_url_name", "dashboard:job:list")
        context.setdefault("is_filters_enabled", True)
        context.setdefault("is_actions_menu_enabled", True)
        context.setdefault("total_records", JobProxy.objects.count())
        context.setdefault("is_header_enabled", True)
        context.setdefault("is_footer_enabled", True)
        context.setdefault("actions_items", "details,update,delete")
        context.setdefault("base_url_name", "dashboard:job")
        context.setdefault("empty_label", _("client"))
        context.setdefault("extra_context", {"is_show_client": True})
        context.setdefault("show_info_icon", True)
        context.setdefault(
            "info_details",
            {
                "tooltip_txt": BW_INFO_MODAL_CSS_CLASSES.get("job").get("tooltip_txt"),
                "modal_css_id": BW_INFO_MODAL_CSS_CLASSES.get("job").get("cssID"),
            },
        )

        # debugging_print(self.filterset.form["name"])
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.user_type == CON_BOOKKEEPER:
            queryset = self.request.user.bookkeeper.get_proxy_model().get_user_jobs()
        self.filterset = JobFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs


class JobCreateView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    CreateView,
):
    # permission_required = ["job.add_job", "job.add_jobproxy"]
    permission_required = "job.add_job"
    permission_denied_message = _("You do not have permission to access this page.")
    template_name = "job/create.html"
    form_class = JobForm
    success_message = _("Job created successfully")
    success_url = reverse_lazy("dashboard:job:list")

    # template_name_suffix = "_create_client"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Create job"))
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"user_type": self.request.user.user_type})
        kwargs.update({"user": self.request.user})
        return kwargs


class JobDetailsView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    DetailView,
):
    # permission_required = ["job.view_job", "job.view_jobproxy"]
    permission_required = "job.view_job"
    permission_denied_message = _("You do not have permission to access this page.")
    template_name = "job/details.html"
    model = JobProxy

    # template_name_suffix = "_create_client"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _(f"Job - {self.get_object().title}"))
        job_update_form = JobForm(
            instance=self.get_object(),
            is_updated=True,
            renderer=BWFormRenderer(),
            client=self.get_object().client,
            # removed_fields=["job"],
        )
        task_form = TaskForm(
            initial={"job": self.get_object(), "client": self.get_object().client},
            # removed_fields=["job"],
            hidden_fields=["job"],
            renderer=BWFormRenderer(),
        )
        document_form = DocumentForm(
            initial={"job": self.get_object(), "document_section": "job"},
            renderer=BWFormRenderer(),
            removed_fields=["client", "task", "status", "job"],
        )
        note_form = NoteForm(
            renderer=BWFormRenderer(),
            initial={"job": self.get_object()},
            removed_fields=["client", "task", "job"],
        )
        special_assignment_form = MiniSpecialAssignmentForm(
            initial={"assigned_by": self.request.user.pk, "job": self.get_object().pk}
        )
        current_user = self.request.user
        # current_user = BWUser.objects.get(pk="907c039a-b151-4faf-aed2-6c30ce4da3a9")
        discussion_initial_data = {
            "job": self.get_object(),
            # "user": self.request.user.pk,
            current_user.get_staff_member_object.get(
                "user_type"
            ): current_user.get_staff_member_object.get("staff_object"),
        }
        # debugging_print(self.request.user.get_staff_member_object)
        # debugging_print(discussion_initial_data)
        discussion_form = DiscussionMiniForm(
            initial=discussion_initial_data,
            # removed_fields=["special_assignment", "replies"],
        )
        context.setdefault("job_update_form", job_update_form)
        context.setdefault("job_status_choices", JobStatusEnum.choices)
        context.setdefault("job_stats_choices", JobStateEnum.choices)
        context.setdefault("task_form", task_form)
        context.setdefault("document_form", document_form)
        context.setdefault("note_form", note_form)
        context.setdefault("discussion_form", discussion_form)
        context.setdefault("special_assignment_form", special_assignment_form)
        return context


class JobUpdateView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    UpdateReturnPreviousMixin,
    UpdateView,
):
    # permission_required = ["job.change_job", "job.change_jobproxy"]
    permission_required = "job.change_job"
    permission_denied_message = _("You do not have permission to access this page.")
    template_name = "job/update.html"
    form_class = JobForm
    success_message = _("Job updated successfully")
    # success_url = reverse_lazy("dashboard:job:list")
    model = JobProxy
    BASE_SUCCESS_URL = "dashboard:job:list"

    # template_name_suffix = "_create_client"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Update job"))
        return context


class JobDeleteView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWCacheViewMixin,
    BWBaseListViewMixin,
    SuccessMessageMixin,
    DeleteView,
):
    template_name = "job/delete.html"
    # permission_required = ["job.delete_job", "job.delete_jobproxy"]
    permission_required = "job.delete_job"
    permission_denied_message = _("You do not have permission to access this page.")
    model = TaskProxy
    success_message = _("Job deleted successfully")
    success_url = reverse_lazy("dashboard:job:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Delete job"))
        return context
