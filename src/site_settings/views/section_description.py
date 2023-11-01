from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import UpdateView, CreateView, ListView

from core.cache import BWCacheViewMixin
from core.views.mixins import BWLoginRequiredMixin, BWBaseListViewMixin
from site_settings.forms import SectionDescriptionForm
from site_settings.models import SectionDescription


class SectionDescriptionCreateView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    CreateView,
):
    permission_required = "manager.manager_user"
    permission_denied_message = _("You do not have permission to access this page.")
    template_name = "site_settings/section_description/create.html"
    form_class = SectionDescriptionForm
    success_message = _("Section descriptions created successfully")
    success_url = reverse_lazy("dashboard:site_settings:section_description:list")
    model = SectionDescription

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Create new description for section"))
        return context


class SectionDescriptionUpdateView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    UpdateView,
):
    # pk_url_kwarg = "slug"
    permission_required = "manager.manager_user"
    permission_denied_message = _("You do not have permission to access this page.")
    template_name = "site_settings/section_description/update.html"
    form_class = SectionDescriptionForm
    success_message = _("Section descriptions updated successfully")
    success_url = reverse_lazy("dashboard:site_settings:section_description:list")
    model = SectionDescription

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Update section descriptions settings"))
        return context


class SectionDescriptionListView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWCacheViewMixin,
    BWBaseListViewMixin,
    ListView,
):
    permission_required = "manager.manager_user"

    permission_denied_message = _("You do not have permission to access this page.")
    template_name = "core/crudl/list.html"
    model = SectionDescription
    list_type = "list"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = _("sections descriptions".capitalize())
        context.setdefault("list_type", self.list_type)
        context.setdefault("page_header", _("sections descriptions".title()))
        context.setdefault(
            "component_path",
            "bw_components/site_settings/section_description/table_list.html",
        )
        context.setdefault("badge_txt", _("Management"))
        context.setdefault(
            "subtitle", _("describe every section in the web application".title())
        )
        context.setdefault(
            "actions_base_url", "dashboard:site_settings:section_description"
        )
        # context.setdefault("filter_cancel_url", "dashboard:site_settings:section_description:list")
        context.setdefault("table_header_title", _("C"))
        context.setdefault("table_header_subtitle", _("description subtitle"))
        context.setdefault("is_show_create_btn", True)
        context.setdefault("pagination_list_url_name", "dashboard:site_settings:section_description:list")
        context.setdefault("is_filters_enabled", False)
        context.setdefault("is_actions_menu_enabled", True)
        context.setdefault("is_header_enabled", True)
        context.setdefault("is_footer_enabled", True)
        context.setdefault("actions_items", "update,")
        context.setdefault("base_url_name", "dashboard:site_settings:section_description")
        context.setdefault("empty_label", _("descriptions"))
        context.setdefault("extra_context", {"is_show_section": True})

        # debugging_print(self.filterset.form["name"])
        return context
