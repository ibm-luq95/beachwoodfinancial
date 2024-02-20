from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from core.cache import BWCacheViewMixin
from core.constants import LIST_VIEW_PAGINATE_BY
from core.constants.css_classes import BW_INFO_MODAL_CSS_CLASSES
from core.constants.users import CON_BOOKKEEPER
from core.views.mixins import BWLoginRequiredMixin, BWBaseListViewMixin
from core.views.mixins.bookkeeper_pass_related_mixin import BookkeeperPassRelatedMixin
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
	permission_required = "task.can_view_list"
	permission_denied_message = _("You do not have permission to access this page.")
	template_name = "core/crudl/list.html"
	model = TaskProxy
	paginate_by = LIST_VIEW_PAGINATE_BY
	list_type = "list"

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		context["title"] = _("Tasks")
		context.setdefault("filter_form", self.filterset.form)
		context.setdefault("list_type", self.list_type)
		context.setdefault("page_header", _("Tasks".title()))
		context.setdefault("component_path", "bw_components/task/table_list.html")
		context.setdefault("subtitle", _("tasks".title()))
		context.setdefault("actions_base_url", "dashboard:task")
		context.setdefault("filter_cancel_url", "dashboard:task:list")
		context.setdefault("table_header_title", _("C"))
		context.setdefault("table_header_subtitle", _("Tasks subtitle"))
		context.setdefault("is_show_create_btn", True)
		context.setdefault("pagination_list_url_name", "dashboard:task:list")
		context.setdefault("is_filters_enabled", True)
		context.setdefault("is_actions_menu_enabled", True)
		context.setdefault("is_header_enabled", True)
		context.setdefault("is_footer_enabled", True)
		context.setdefault("actions_items", "update,delete")
		context.setdefault("base_url_name", "dashboard:task")
		context.setdefault("empty_label", _("task"))
		context.setdefault(
			"extra_context",
			{
				"is_show_status_column": True,
				"is_show_type_column": True,
				"is_show_manager_column": True,
				"is_show_job_column": True,
			},
		)
		context.setdefault("show_info_icon", True)
		context.setdefault(
			"info_details",
			{
				"tooltip_txt": BW_INFO_MODAL_CSS_CLASSES.get("task").get("tooltip_txt"),
				"modal_css_id": BW_INFO_MODAL_CSS_CLASSES.get("task").get("cssID"),
			},
		)

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
	BookkeeperPassRelatedMixin,
	CreateView,
):
	# permission_required = ["task.add_taskproxy", "task.add_task"]
	permission_required = "task.add_task"
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
	BookkeeperPassRelatedMixin,
	UpdateView,
):
	# permission_required = ["task.change_taskproxy", "task.change_task"]
	permission_required = "task.change_task"
	permission_denied_message = _("You do not have permission to access this page.")
	template_name = "task/update.html"
	form_class = TaskForm
	success_message = _("Task updated successfully")
	# success_url = reverse_lazy("dashboard:task:list")
	model = TaskProxy

	# template_name_suffix = "_create_client"

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		context.setdefault("title", _("Update task"))
		prev_url = self.request.META.get("HTTP_REFERER")
		self.request.session["prev_url"] = prev_url
		self.request.session.modified = True

		return context

	def get_success_url(self) -> str:
		"""Return the URL to redirect to after processing a valid form."""
		prev_url = self.request.session.get("prev_url")
		self.request.session.delete("prev_url")
		self.request.session.modified = True
		if prev_url is not None:
			return str(prev_url)  # success_url may be lazy
		else:
			return reverse_lazy("dashboard:task:list")


class TaskDeleteView(
	PermissionRequiredMixin,
	BWLoginRequiredMixin,
	BWCacheViewMixin,
	BWBaseListViewMixin,
	SuccessMessageMixin,
	DeleteView,
):
	# permission_required = ["task.delete_taskproxy", "task.delete_task"]
	permission_required = "task.delete_task"
	permission_denied_message = _("You do not have permission to access this page.")
	template_name = "core/crudl/delete.html"
	model = TaskProxy
	success_message = _("Task deleted successfully")
	success_url = reverse_lazy("dashboard:task:list")

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		context.setdefault("title", _("Delete task"))
		context.setdefault("cancel_url", "dashboard:task:list")
		context.setdefault("object", self.get_object())
		context.setdefault("object_name", "task")
		context.setdefault("form_css_id", "taskDeleteForm")
		return context
