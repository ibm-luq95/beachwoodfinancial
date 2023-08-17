from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
    RedirectView,
    FormView,
)
from django.utils.translation import gettext as _

from beach_wood_user.models import BWUser
from core.cache import BWCacheViewMixin
from core.choices import JobStatusEnum
from core.config.forms import BWFormRenderer
from core.constants import LIST_VIEW_PAGINATE_BY
from core.utils import debugging_print
from core.views.mixins import (
    BWLoginRequiredMixin,
    BWBaseListViewMixin,
    BWManagerAccessMixin,
)
from discussion.forms import DiscussionForm, DiscussionMiniForm
from document.forms import DocumentForm
from job.filters import JobFilter
from job.forms import JobForm
from job.models import JobProxy
from note.forms import NoteForm
from note.models import Note
from special_assignment.forms import SpecialAssignmentForm, MiniSpecialAssignmentForm
from task.forms import TaskForm
from task.models import TaskProxy


class JobListView(
    BWLoginRequiredMixin,
    BWManagerAccessMixin,
    BWCacheViewMixin,
    BWBaseListViewMixin,
    ListView,
):
    # permission_required = "client.can_view_list"
    template_name = "job/list.html"
    model = JobProxy
    paginate_by = LIST_VIEW_PAGINATE_BY
    list_type = "list"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = _("Jobs")
        context.setdefault("filter_form", self.filterset.form)
        context.setdefault("list_type", self.list_type)
        context.setdefault("page_header", "Tasks".title())

        # debugging_print(self.filterset.form["name"])
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = JobFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs


class JobCreateView(
    BWLoginRequiredMixin,
    BWManagerAccessMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    CreateView,
):
    # permission_required = "client.add_client"
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


class JobDetailsView(
    BWLoginRequiredMixin,
    BWManagerAccessMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    DetailView,
):
    # permission_required = "client.add_client"
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
            removed_fields=["client", "task", "status", "job", "document_section"],
        )
        note_form = NoteForm(
            renderer=BWFormRenderer(),
            initial={"job": self.get_object(), "note_section": "note"},
            removed_fields=["client", "task", "note_section", "job"],
        )
        special_assignment_form = MiniSpecialAssignmentForm(
            initial={"assigned_by": self.request.user.pk}
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
        context.setdefault("task_form", task_form)
        context.setdefault("document_form", document_form)
        context.setdefault("note_form", note_form)
        context.setdefault("discussion_form", discussion_form)
        context.setdefault("special_assignment_form", special_assignment_form)
        return context


class JobUpdateView(
    BWLoginRequiredMixin,
    BWManagerAccessMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    UpdateView,
):
    # permission_required = "client.add_client"
    template_name = "job/update.html"
    form_class = JobForm
    success_message = _("Job updated successfully")
    success_url = reverse_lazy("dashboard:job:list")
    model = JobProxy

    # template_name_suffix = "_create_client"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Update job"))
        return context


class JobDeleteView(
    BWLoginRequiredMixin,
    BWManagerAccessMixin,
    BWCacheViewMixin,
    BWBaseListViewMixin,
    SuccessMessageMixin,
    DeleteView,
):
    template_name = "job/delete.html"
    # form_class = ClientCategoryForm
    model = TaskProxy
    success_message = _("Job deleted successfully")
    success_url = reverse_lazy("dashboard:job:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Delete job"))
        return context
