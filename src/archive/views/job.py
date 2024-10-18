# -*- coding: utf-8 -*-#
from django.utils.translation import gettext as _
from django.views.generic import (
    ListView,
)

from core.cache import BWCacheViewMixin
from core.constants import LIST_VIEW_PAGINATE_BY
from core.constants.users import CON_BOOKKEEPER
from core.views.mixins import BWLoginRequiredMixin, BWBaseListViewMixin
from job.filters import JobFilter
from job.models import JobProxy


class JobArchiveListView(
    BWLoginRequiredMixin, BWCacheViewMixin, BWBaseListViewMixin, ListView
):
    template_name = "core/crudl/list.html"
    model = JobProxy
    paginate_by = LIST_VIEW_PAGINATE_BY
    list_type = "archive"
    queryset = JobProxy.archive_objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        context["title"] = _("Jobs archive")
        context.setdefault("component_path", "bw_components/archive/job/table_list.html")
        context.setdefault("filter_form", self.filterset.form)
        context.setdefault("list_type", self.list_type)
        context.setdefault("page_header", "jobs archive".title())
        context.setdefault("subtitle", "Archived jobs".title())
        context.setdefault("actions_base_url", "dashboard:job")
        context.setdefault("filter_cancel_url", "dashboard:archive:jobs:list")
        context.setdefault("table_header_title", _("C"))
        context.setdefault("table_header_subtitle", _("Jobs archive subtitle"))
        context.setdefault("is_show_create_btn", False)
        context.setdefault("pagination_list_url_name", "dashboard:archive:jobs:list")
        context.setdefault("is_filters_enabled", True)
        context.setdefault("is_actions_menu_enabled", False)
        context.setdefault("is_header_enabled", True)
        context.setdefault("is_footer_enabled", True)
        # context.setdefault("actions_items", "details,update,delete")
        context.setdefault("base_url_name", "dashboard:job")
        context.setdefault("extra_context", {"is_show_client": True})
        context.setdefault("empty_label", _("job(s)"))
        context.setdefault("show_info_icon", False)
        # context.setdefault(
        #     "info_details",
        #     {
        #         "tooltip_txt": BW_INFO_MODAL_CSS_CLASSES.get("client").get("tooltip_txt"),
        #         "modal_css_id": BW_INFO_MODAL_CSS_CLASSES.get("client").get("cssID"),
        #     },
        # )

        # debugging_print(self.filterset.form["name"])
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.user_type == CON_BOOKKEEPER:
            queryset = self.request.user.bookkeeper.get_proxy_model().get_user_jobs(
                is_archived=True
            )
        self.filterset = JobFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs
