# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView
from django.utils.translation import gettext as _

from core.cache import BWSiteSettingsViewMixin
from core.constants import LIST_VIEW_PAGINATE_BY
from core.constants.css_classes import BW_INFO_MODAL_CSS_CLASSES
from core.constants.users import CON_BOOKKEEPER
from core.views.mixins import BWLoginRequiredMixin, BWBaseListViewMixin
from task.filters import TaskFilter
from task.models import TaskProxy


class TaskArchiveListView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWSiteSettingsViewMixin,
    BWBaseListViewMixin,
    ListView,
):
    permission_required = "task.can_view_list"
    permission_denied_message = _("You do not have permission to access this page.")
    template_name = "core/crudl/list.html"
    model = TaskProxy
    paginate_by = LIST_VIEW_PAGINATE_BY
    list_type = "archive"
    queryset = TaskProxy.archive_objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = _("Tasks archive")
        context.setdefault("filter_form", self.filterset.form)
        context.setdefault("list_type", self.list_type)
        context.setdefault("page_header", _("Tasks archive".capitalize()))
        context.setdefault("component_path", "bw_components/task/table_list.html")
        context.setdefault("subtitle", _("tasks".title()))
        context.setdefault("actions_base_url", "dashboard:task")
        context.setdefault("filter_cancel_url", "dashboard:archive:tasks:list")
        context.setdefault("table_header_title", _("C"))
        context.setdefault("table_header_subtitle", _("Tasks subtitle"))
        context.setdefault("is_show_create_btn", True)
        context.setdefault("pagination_list_url_name", "dashboard:archive:tasks:list")
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
