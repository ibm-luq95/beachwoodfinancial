from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from core.cache import BWCacheViewMixin
from core.constants import LIST_VIEW_PAGINATE_BY
from core.constants.users import CON_BOOKKEEPER
from core.views.mixins import BWLoginRequiredMixin, BWBaseListViewMixin
from task.filters import TaskFilter
from task.forms import TaskForm
from task.models import TaskProxy


class TaskListView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWCacheViewMixin,
    BWBaseListViewMixin,
    ListView,
):
    permission_required = ["task.can_view_list"]
    permission_denied_message = _("You do not have permission to access this page.")
    template_name = "task/list.html"
    model = TaskProxy
    paginate_by = LIST_VIEW_PAGINATE_BY
    list_type = "list"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = _("Tasks")
        context.setdefault("filter_form", self.filterset.form)
        context.setdefault("list_type", self.list_type)
        context.setdefault("page_header", "Tasks".title())

        # debugging_print(self.filterset.form["name"])
        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.request.user.user_type == CON_BOOKKEEPER:
            queryset = (
                self.request.user.bookkeeper.get_proxy_model().get_all_related_items(
                    "tasks"
                )
            )

        self.filterset = TaskFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs


class TaskCreateView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    CreateView,
):
    permission_required = ["task.add_taskproxy", "task.add_task"]
    permission_denied_message = _("You do not have permission to access this page.")
    template_name = "task/create.html"
    form_class = TaskForm
    success_message = _("Task created successfully")
    success_url = reverse_lazy("dashboard:task:list")

    # template_name_suffix = "_create_client"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Create task"))
        return context


class TaskUpdateView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    UpdateView,
):
    permission_required = ["task.change_taskproxy", "task.change_task"]
    permission_denied_message = _("You do not have permission to access this page.")
    template_name = "task/update.html"
    form_class = TaskForm
    success_message = _("Task updated successfully")
    success_url = reverse_lazy("dashboard:task:list")
    model = TaskProxy

    # template_name_suffix = "_create_client"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Update task"))
        return context


class TaskDeleteView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWCacheViewMixin,
    BWBaseListViewMixin,
    SuccessMessageMixin,
    DeleteView,
):
    permission_required = ["task.delete_taskproxy", "task.delete_task"]
    permission_denied_message = _("You do not have permission to access this page.")
    template_name = "task/delete.html"
    model = TaskProxy
    success_message = _("Task deleted successfully")
    success_url = reverse_lazy("dashboard:task:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Delete task"))
        return context
