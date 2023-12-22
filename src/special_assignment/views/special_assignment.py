# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from core.cache import BWCacheViewMixin
from core.constants import LIST_VIEW_PAGINATE_BY
from core.constants.css_classes import BW_INFO_MODAL_CSS_CLASSES
from core.constants.status_labels import CON_ARCHIVED, CON_COMPLETED
from core.constants.users import CON_BOOKKEEPER
from core.views.mixins import BWLoginRequiredMixin, BWBaseListViewMixin
from core.views.mixins.update_previous_mixin import UpdateReturnPreviousMixin
from special_assignment.filters import SpecialAssignmentFilter
from special_assignment.forms import SpecialAssignmentForm
from special_assignment.models import SpecialAssignmentProxy


class SpecialAssignmentListView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWCacheViewMixin,
    BWBaseListViewMixin,
    ListView,
):
    permission_required = "special_assignment.can_view_list"
    template_name = "core/crudl/list.html"
    model = SpecialAssignmentProxy
    paginate_by = LIST_VIEW_PAGINATE_BY
    list_type = "list"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = _("Special assignments")
        context.setdefault("filter_form", self.filterset.form)
        context.setdefault("list_type", self.list_type)
        context.setdefault("page_header", _("Special assignments".title()))
        context.setdefault(
            "component_path", "bw_components/special_assignment/table_list.html"
        )
        context.setdefault(
            "subtitle",
            _("Special assignments custom specific assignments to clients".title()),
        )
        context.setdefault("actions_base_url", "dashboard:special_assignment")
        context.setdefault("filter_cancel_url", "dashboard:special_assignment:list")
        context.setdefault("table_header_title", _("C"))
        context.setdefault("table_header_subtitle", _("Jobs subtitle"))
        context.setdefault("is_show_create_btn", True)
        context.setdefault("pagination_list_url_name", "dashboard:special_assignment:list")
        context.setdefault("is_filters_enabled", True)
        context.setdefault("is_actions_menu_enabled", True)
        context.setdefault("is_header_enabled", True)
        context.setdefault("is_footer_enabled", True)
        context.setdefault("actions_items", "details,update,delete")
        context.setdefault("base_url_name", "dashboard:special_assignment")
        context.setdefault("empty_label", _("assignments"))
        context.setdefault("extra_context", {})
        context.setdefault("show_info_icon", True)
        context.setdefault(
            "info_details",
            {
                "tooltip_txt": BW_INFO_MODAL_CSS_CLASSES.get("special_assignment").get(
                    "tooltip_txt"
                ),
                "modal_css_id": BW_INFO_MODAL_CSS_CLASSES.get("special_assignment").get(
                    "cssID"
                ),
            },
        )

        # debugging_print(self.filterset.form["name"])
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.user_type == CON_BOOKKEEPER:
            queryset = (
                self.request.user.bookkeeper.get_proxy_model().special_assignments.all()
            )
        self.filterset = SpecialAssignmentFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs


class SpecialAssignmentCreateView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    CreateView,
):
    # permission_required = [
    #     "special_assignment.add_specialassignmentproxy",
    #     "special_assignment.add_specialassignment",
    # ]
    permission_required = "special_assignment.add_specialassignment"
    template_name = "special_assignment/create.html"
    form_class = SpecialAssignmentForm
    success_message = _("Special assignment created successfully")
    success_url = reverse_lazy("dashboard:special_assignment:list")

    # template_name_suffix = "_create_client"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Create assignment"))
        return context

    def get_initial(self) -> dict:
        initial = super().get_initial()
        initial.setdefault("assigned_by", self.request.user)

        return initial


class SpecialAssignmentUpdateView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    UpdateReturnPreviousMixin,
    UpdateView,
):
    # permission_required = [
    #     "special_assignment.change_specialassignment",
    #     "special_assignment.change_specialassignmentproxy",
    # ]
    permission_required = "special_assignment.change_specialassignment"
    template_name = "special_assignment/update.html"
    form_class = SpecialAssignmentForm
    success_message = _("Special assignment updated successfully")
    # success_url = reverse_lazy("dashboard:special_assignment:list")
    model = SpecialAssignmentProxy
    BASE_SUCCESS_URL = "dashboard:special_assignment:list"

    # template_name_suffix = "_create_client"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Update special assignment"))

        return context


class SpecialAssignmentDeleteView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    DeleteView,
):
    # permission_required = [
    #     "special_assignment.delete_specialassignment",
    #     "special_assignment.delete_specialassignmentproxy",
    # ]
    permission_required = "special_assignment.delete_specialassignment"
    template_name = "special_assignment/delete.html"
    model = SpecialAssignmentProxy
    success_message = _("Special assignment deleted successfully")
    success_url = reverse_lazy("dashboard:special_assignment:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Delete special assignment"))
        return context


class SpecialAssignmentDetailsView(
    PermissionRequiredMixin, BWLoginRequiredMixin, BWCacheViewMixin, DetailView
):
    model = SpecialAssignmentProxy
    template_name = "special_assignment/details.html"
    # permission_required = [
    #     "special_assignment.view_specialassignment",
    #     "special_assignment.view_specialassignmentproxy",
    # ]
    permission_required = "special_assignment.view_specialassignment"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("SA - ") + self.get_object().title)
        return context


class RequestedSpecialAssignmentsListView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWCacheViewMixin,
    BWBaseListViewMixin,
    ListView,
):
    permission_required = "special_assignment.can_view_list"
    template_name = "core/crudl/list.html"

    model = SpecialAssignmentProxy
    http_method_names = ["get"]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("All requested special assignment"))
        context.setdefault("page_header", "requestes assignments".capitalize())
        context.setdefault("filter_form", self.filterset.form)
        context.setdefault("filter_form", self.filterset.form)
        context.setdefault("page_header", _("requestes assignments".capitalize()))
        context.setdefault(
            "component_path", "bw_components/special_assignment/table_list.html"
        )
        context.setdefault(
            "subtitle",
            _("Special assignments custom specific assignments to clients".title()),
        )
        context.setdefault("actions_base_url", "dashboard:special_assignment")
        context.setdefault("filter_cancel_url", "dashboard:special_assignment:list")
        context.setdefault("table_header_title", _("C"))
        context.setdefault("table_header_subtitle", _("Jobs subtitle"))
        context.setdefault("is_show_create_btn", True)
        context.setdefault("pagination_list_url_name", "dashboard:special_assignment:list")
        context.setdefault("is_filters_enabled", True)
        context.setdefault("is_actions_menu_enabled", True)
        context.setdefault("is_header_enabled", True)
        context.setdefault("is_footer_enabled", True)
        context.setdefault("actions_items", "details,update,delete")
        context.setdefault("base_url_name", "dashboard:special_assignment")
        context.setdefault("empty_label", _("assignments"))
        context.setdefault("extra_context", {})
        context.setdefault("show_info_icon", True)
        context.setdefault(
            "info_details",
            {
                "tooltip_txt": BW_INFO_MODAL_CSS_CLASSES.get("requested_assignment").get(
                    "tooltip_txt"
                ),
                "modal_css_id": BW_INFO_MODAL_CSS_CLASSES.get("requested_assignment").get(
                    "cssID"
                ),
            },
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        current_user = self.request.user
        manager = None
        if hasattr(current_user, "manager"):
            manager = self.request.user.manager
        elif hasattr(current_user, "bookkeeper"):
            manager = self.request.user.bookkeeper
        elif hasattr(current_user, "assistant"):
            manager = self.request.user.assistant
        queryset = manager.user.requested_assignments.filter(
            ~Q(status__in=[CON_ARCHIVED, CON_COMPLETED])
        )
        self.filterset = SpecialAssignmentFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs
