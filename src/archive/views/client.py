# -*- coding: utf-8 -*-#

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils.translation import gettext as _
from django.views.generic import ListView

from client.filters import ClientFilter
from client.models import ClientProxy
from core.cache import BWSiteSettingsViewMixin
from core.constants import LIST_VIEW_PAGINATE_BY
from core.constants.css_classes import BW_INFO_MODAL_CSS_CLASSES
from core.constants.status_labels import CON_COMPLETED, CON_ARCHIVED
from core.constants.users import CON_BOOKKEEPER
from core.views.mixins import BWBaseListViewMixin, BWLoginRequiredMixin


class ClientArchiveListView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWSiteSettingsViewMixin,
    BWBaseListViewMixin,
    ListView,
):
    permission_required = "client.can_view_list"
    permission_denied_message = _("You do not have permission to access this page.")
    template_name = "core/crudl/list.html"
    model = ClientProxy
    # queryset = Client.objects.filter(~Q(status="archive")).prefetch_related("jobs")
    # queryset = Client.objects.prefetch_related(
    #     "jobs", "jobs__created_by", "important_contacts"
    # ).filter(~Q(status=CON_ARCHIVED))
    paginate_by = LIST_VIEW_PAGINATE_BY
    queryset = ClientProxy.archive_objects.all()
    list_type = "archive"
    is_show_create_btn = False
    is_filters_enabled = True
    is_actions_menu_enabled = True
    is_header_enabled = True
    is_footer_enabled = True
    show_info_icon = False
    page_title = _("Clients archive")
    page_header = _("Clients archive".title())
    component_path = "bw_components/client/table_list.html"
    actions_base_url = "dashboard:archive:clients"
    filter_cancel_url = "dashboard:archive:clients:list"
    table_header_title = _("C")
    pagination_list_url_name = "dashboard:archive:clients:list"
    actions_items = "details,update,delete"
    base_url_name = "dashboard:archive:clients"
    empty_label = _("client(s)")
    subtitle = _("Client archive".title())

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # context.setdefault("filter_form", self.filterset.form)
        context.setdefault(
            "extra_context", {"is_show_bookkeeper": True, "is_show_status": True}
        )
        context.setdefault(
            "info_details",
            {
                "tooltip_txt": BW_INFO_MODAL_CSS_CLASSES.get("client").get("tooltip_txt"),
                "modal_css_id": BW_INFO_MODAL_CSS_CLASSES.get("client").get("cssID"),
            },
        )

        # debugging_print(self.filterset.form["name"])
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.user_type == CON_BOOKKEEPER:
            queryset = self.request.user.bookkeeper.get_proxy_model().clients.filter(
                status__in=[CON_ARCHIVED, CON_COMPLETED]
            )
        self.filterset = ClientFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs
