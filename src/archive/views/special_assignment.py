# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils.translation import gettext as _
from django.views.generic import ListView

from core.cache import BWCacheViewMixin
from core.constants import LIST_VIEW_PAGINATE_BY
from core.constants.css_classes import BW_INFO_MODAL_CSS_CLASSES
from core.constants.users import CON_BOOKKEEPER
from core.views.mixins import BWLoginRequiredMixin, BWBaseListViewMixin
from special_assignment.filters import SpecialAssignmentFilter
from special_assignment.models import SpecialAssignmentProxy


class SpecialAssignmentArchiveListView(
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
    list_type = "archive"
    queryset = SpecialAssignmentProxy.archive_objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = _("Special assignments archive")
        context.setdefault("filter_form", self.filterset.form)
        context.setdefault("list_type", self.list_type)
        context.setdefault("page_header", _("Special assignments archived".capitalize()))
        context.setdefault(
            "component_path", "bw_components/special_assignment/table_list.html"
        )
        context.setdefault(
            "subtitle",
            _("Special assignments custom specific assignments to clients".title()),
        )
        context.setdefault("actions_base_url", "dashboard:special_assignment")
        context.setdefault("filter_cancel_url", "dashboard:archive:special_assignment:list")
        context.setdefault("table_header_title", _("C"))
        context.setdefault("table_header_subtitle", _("Jobs subtitle"))
        context.setdefault("is_show_create_btn", True)
        context.setdefault("pagination_list_url_name", "dashboard:archive:special_assignment:list")
        context.setdefault("is_filters_enabled", True)
        context.setdefault("is_actions_menu_enabled", True)
        context.setdefault("is_header_enabled", True)
        context.setdefault("is_footer_enabled", True)
        context.setdefault("actions_items", "details,update,delete")
        context.setdefault("base_url_name", "dashboard:special_assignment")
        context.setdefault("empty_label", _("assignment(s)"))
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
