# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils.translation import gettext as _
from django.views.generic import ListView

from core.cache import BWCacheViewMixin
from core.constants import LIST_VIEW_PAGINATE_BY
from core.constants.css_classes import BW_INFO_MODAL_CSS_CLASSES
from core.views.mixins import BWLoginRequiredMixin, BWBaseListViewMixin
from discussion.models import DiscussionProxy


class DiscussionListView(
	PermissionRequiredMixin,
	BWLoginRequiredMixin,
	BWCacheViewMixin,
	BWBaseListViewMixin,
	ListView,
):
	permission_required = "discussion.can_view_list"
	template_name = "core/crudl/list.html"
	model = DiscussionProxy
	paginate_by = LIST_VIEW_PAGINATE_BY
	list_type = "list"

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		context["title"] = _("Discussions")
		# context.setdefault("filter_form", self.filterset.form)
		context.setdefault("list_type", self.list_type)
		context.setdefault("page_header", _("discussions".title()))
		context.setdefault("component_path", "bw_components/discussion/table_list.html")
		context.setdefault(
			"subtitle",
			_("Discussions for all jobs and special assignments".title()),
		)
		context.setdefault("actions_base_url", "dashboard:discussion")
		context.setdefault("filter_cancel_url", "dashboard:discussion:list")
		context.setdefault("table_header_title", _("C"))
		context.setdefault("table_header_subtitle", _("Jobs subtitle"))
		context.setdefault("is_show_create_btn", False)
		context.setdefault("pagination_list_url_name", "dashboard:discussion:list")
		context.setdefault("is_filters_enabled", False)
		context.setdefault("is_actions_menu_enabled", False)
		context.setdefault("is_header_enabled", True)
		context.setdefault("is_footer_enabled", True)
		context.setdefault("actions_items", "details,update,delete")
		context.setdefault("base_url_name", "dashboard:discussion")
		context.setdefault("empty_label", _("discussions"))
		context.setdefault("extra_context", {})
		context.setdefault("show_info_icon", True)
		context.setdefault(
			"info_details",
			{
				"tooltip_txt": BW_INFO_MODAL_CSS_CLASSES.get("discussion").get(
					"tooltip_txt"
				),
				"modal_css_id": BW_INFO_MODAL_CSS_CLASSES.get("discussion").get("cssID"),
			},
		)

		# debugging_print(self.filterset.form["name"])
		return context
