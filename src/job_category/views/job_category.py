from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from core.cache import BWCacheViewMixin
from core.constants import LIST_VIEW_PAGINATE_BY
from core.constants.css_classes import BW_INFO_MODAL_CSS_CLASSES
from core.views.mixins import BWLoginRequiredMixin, BWBaseListViewMixin
from job_category.forms import JobCategoryForm
from job_category.models import JobCategory


class JobCategoryListView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWCacheViewMixin,
    BWBaseListViewMixin,
    ListView,
):
    permission_required = "job_category.can_view_list"
    permission_denied_message = _("You do not have permission to access this page.")
    template_name = "core/crudl/list.html"
    model = JobCategory
    paginate_by = LIST_VIEW_PAGINATE_BY
    list_type = "list"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = _("Job categories")
        context.setdefault("list_type", self.list_type)
        context.setdefault("page_header", _("Jobs categories".title()))
        context.setdefault("component_path", "bw_components/job_category/table_list.html")
        context.setdefault("subtitle", _("job_category".title()))
        context.setdefault("actions_base_url", "dashboard:job_category")
        context.setdefault("filter_cancel_url", "dashboard:job_category:list")
        context.setdefault("table_header_title", _("C"))
        context.setdefault("table_header_subtitle", _("job_categorys subtitle"))
        context.setdefault("is_show_create_btn", True)
        context.setdefault("pagination_list_url_name", "dashboard:job_category:list")
        context.setdefault("is_filters_enabled", False)
        context.setdefault("is_actions_menu_enabled", True)
        context.setdefault("is_header_enabled", True)
        context.setdefault("is_footer_enabled", True)
        context.setdefault("actions_items", "update,delete")
        context.setdefault("base_url_name", "dashboard:job_category")
        context.setdefault("empty_label", _("categories"))
        context.setdefault("extra_context", {})
        context.setdefault("show_info_icon", True)
        context.setdefault(
            "info_details",
            {
                "tooltip_txt": BW_INFO_MODAL_CSS_CLASSES.get("job_category").get(
                    "tooltip_txt"
                ),
                "modal_css_id": BW_INFO_MODAL_CSS_CLASSES.get("job_category").get("cssID"),
            },
        )

        return context


class JobCategoryCreateView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    CreateView,
):
    permission_required = "job_category.add_jobcategory"
    permission_denied_message = _("You do not have permission to access this page.")
    template_name = "job_category/create.html"
    form_class = JobCategoryForm
    success_message = _("Job category created successfully")
    success_url = reverse_lazy("dashboard:job_category:list")

    # template_name_suffix = "_create_client"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Create note"))
        return context


class JobCategoryUpdateView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    UpdateView,
):
    permission_required = "job_category.change_jobcategory"
    permission_denied_message = _("You do not have permission to access this page.")
    template_name = "job_category/update.html"
    form_class = JobCategoryForm
    success_message = _("Category updated successfully")
    success_url = reverse_lazy("dashboard:job_category:list")
    model = JobCategory

    # template_name_suffix = "_create_client"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Update category"))
        return context


class JobCategoryDeleteView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    DeleteView,
):
    permission_required = "job_category.delete_jobcategory"
    permission_denied_message = _("You do not have permission to access this page.")
    template_name = "job_category/delete.html"
    model = JobCategory
    success_message = _("Job category deleted successfully")
    success_url = reverse_lazy("dashboard:job_category:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Delete note"))
        return context
