# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from core.cache import BWSiteSettingsViewMixin
from core.constants import LIST_VIEW_PAGINATE_BY
from core.constants.css_classes import BW_INFO_MODAL_CSS_CLASSES
from core.views.mixins import BWLoginRequiredMixin, BWBaseListViewMixin
from staff_briefcase.forms import (
    BriefcaseNoteMiniForm,
    BriefcaseDocumentMiniForm,
    BriefcaseAccountMiniForm,
)
from staff_briefcase.models import StaffBriefcase


class StaffBriefcaseListView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWSiteSettingsViewMixin,
    BWBaseListViewMixin,
    ListView,
):
    permission_required = "staff_briefcase.can_view_list"
    template_name = "core/crudl/list.html"
    model = StaffBriefcase
    paginate_by = LIST_VIEW_PAGINATE_BY
    list_type = "list"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = _("Staff Briefcases")
        # context.setdefault("filter_form", self.filterset.form)
        context.setdefault("list_type", self.list_type)
        context.setdefault("page_header", _("Briefcases".title()))
        context.setdefault(
            "component_path", "bw_components/staff_briefcase/table_list.html"
        )
        context.setdefault(
            "subtitle",
            _(
                "Briefcases include documents and notes belongs to staff members".capitalize()
            ),
        )
        context.setdefault("actions_base_url", "dashboard:briefcase")
        context.setdefault("filter_cancel_url", "dashboard:special_assignment:list")
        context.setdefault("table_header_title", _("C"))
        context.setdefault("table_header_subtitle", _("Briefcases subtitle"))
        context.setdefault("is_show_create_btn", True)
        context.setdefault("pagination_list_url_name", "dashboard:briefcase:list")
        context.setdefault("is_filters_enabled", False)
        context.setdefault("is_actions_menu_enabled", True)
        context.setdefault("is_header_enabled", True)
        context.setdefault("is_footer_enabled", True)
        # context.setdefault("actions_items", "details,update,delete")
        context.setdefault("actions_items", "details,")
        context.setdefault("base_url_name", "dashboard:briefcase")
        context.setdefault("empty_label", _("briefcases"))
        context.setdefault("extra_context", {})
        context.setdefault("show_info_icon", True)
        context.setdefault(
            "info_details",
            {
                "tooltip_txt": BW_INFO_MODAL_CSS_CLASSES.get("staff_briefcase").get(
                    "tooltip_txt"
                ),
                "modal_css_id": BW_INFO_MODAL_CSS_CLASSES.get("staff_briefcase").get(
                    "cssID"
                ),
            },
        )

        # debugging_print(self.filterset.form["name"])
        return context

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     if self.request.user.user_type == CON_BOOKKEEPER:
    #         queryset = (
    #             self.request.user.bookkeeper.get_proxy_model().special_assignments.all()
    #         )
    #     self.filterset = SpecialAssignmentFilter(self.request.GET, queryset=queryset)
    #     return self.filterset.qs


class StaffBriefcaseDetailView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWSiteSettingsViewMixin,
    DetailView,
):
    permission_required = "staff_briefcase.view_staffbriefcase"
    template_name = "staff_briefcase/details.html"
    model = StaffBriefcase
    # context_object_name = "briefcase"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = _(f"Briefcase - {self.get_object().user.fullname}")
        briefcase_note_form = BriefcaseNoteMiniForm(
            initial={"briefcase": self.get_object().pk}
        )
        briefcase_document_form = BriefcaseDocumentMiniForm(
            initial={"briefcase": self.get_object().pk}
        )
        briefcase_account_form = BriefcaseAccountMiniForm(
            initial={"briefcase": self.get_object().pk}
        )
        context.setdefault("briefcase_note_form", briefcase_note_form)
        context.setdefault("briefcase_document_form", briefcase_document_form)
        context.setdefault("briefcase_account_form", briefcase_account_form)

        return context


class StaffBriefcaseCreateView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWSiteSettingsViewMixin,
    SuccessMessageMixin,
    CreateView,
):
    permission_required = "staff_briefcase.add_briefcase"
    template_name = "core/crudl/create.html"
    model = StaffBriefcase
