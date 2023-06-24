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

from core.cache import BWCacheViewMixin
from core.choices import JobStatusEnum
from core.constants import LIST_VIEW_PAGINATE_BY
from core.views.mixins import (
    BWLoginRequiredMixin,
    BWBaseListViewMixin,
    BWManagerAccessMixin,
)
from job.filters import JobFilter
from job.forms import JobForm
from job.models import JobProxy
from note.forms import NoteForm
from note.models import Note
from task.filters import TaskFilter
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
        job_update_form = JobForm(instance=self.get_object(), is_updated=True)
        context.setdefault("job_update_form", job_update_form)
        context.setdefault("job_status_choices", JobStatusEnum.choices)
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
    model = Note

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
