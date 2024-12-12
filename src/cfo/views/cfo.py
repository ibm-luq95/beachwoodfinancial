# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db import transaction
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import DeleteView, ListView, FormView
from django.views.generic.detail import SingleObjectMixin

from beach_wood_user.models import BWUser
from bookkeeper.models import BookkeeperProxy
from cfo.filters.cfo import CFOFilter
from cfo.forms.cfo import CFOForm
from cfo.models import CFOProxy
from core.cache import BWSiteSettingsViewMixin
from core.constants import LIST_VIEW_PAGINATE_BY
from core.constants.css_classes import BW_INFO_MODAL_CSS_CLASSES
from core.utils import debugging_print
from core.views.mixins import BWBaseListViewMixin, BWLoginRequiredMixin


class CFOListView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWSiteSettingsViewMixin,
    BWBaseListViewMixin,
    ListView,
):
    permission_required = "cfo.can_view_list"
    template_name = "core/crudl/list.html"
    model = CFOProxy
    paginate_by = LIST_VIEW_PAGINATE_BY
    list_type = "list"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = _("CFOs")
        context.setdefault("filter_form", self.filterset.form)
        context.setdefault("list_type", self.list_type)
        context.setdefault("page_header", _("CFOs"))
        context.setdefault("component_path", "bw_components/cfo/table_list.html")
        context.setdefault("subtitle", _("CFOs staff"))
        context.setdefault("actions_base_url", "dashboard:management_cfo")
        context.setdefault("filter_cancel_url", "dashboard:management_cfo:list")
        context.setdefault("table_header_title", _("C"))
        context.setdefault("table_header_subtitle", _("management_bookkeeper subtitle"))
        context.setdefault("is_show_create_btn", True)
        context.setdefault("pagination_list_url_name", "dashboard:management_cfo:list")
        context.setdefault("is_filters_enabled", True)
        context.setdefault("is_actions_menu_enabled", True)
        context.setdefault("is_header_enabled", True)
        context.setdefault("is_footer_enabled", True)
        context.setdefault("actions_items", "update,delete")
        context.setdefault("base_url_name", "dashboard:management_cfo")
        context.setdefault("empty_label", _("CFOs"))
        context.setdefault("extra_context", {})
        context.setdefault("show_info_icon", True)
        context.setdefault(
            "info_details",
            {
                "tooltip_txt": BW_INFO_MODAL_CSS_CLASSES.get("cfo").get("tooltip_txt"),
                "modal_css_id": BW_INFO_MODAL_CSS_CLASSES.get("cfo").get("cssID"),
            },
        )

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = CFOFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs


class CFOCreateView(
    PermissionRequiredMixin,
    SuccessMessageMixin,
    BWLoginRequiredMixin,
    BWSiteSettingsViewMixin,
    FormView,
):
    permission_required = "cfo.add_cfoproxy"
    permission_denied_message = _("You do not have permission to access this page.")
    template_name = "cfo/create.html"
    form_class = CFOForm
    success_message = _("CFO created successfully")
    success_url = reverse_lazy("dashboard:management_cfo:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Create a new CFO"))
        return context


def form_valid(self, form: CFOForm):
    """If the form is valid, save the associated model."""
    with transaction.atomic():
        user_details = {
            "first_name": form.cleaned_data.get("first_name"),
            "last_name": form.cleaned_data.get("last_name"),
            "email": form.cleaned_data.get("email"),
            "user_type": form.STAFF_MEMBER_TYPE,
        }
        new_user = BWUser.objects.create(**user_details)
        debugging_print(form.cleaned_data.get("password"))
        new_user.set_password(form.cleaned_data.get("password"))
        new_user.save()
        new_user.cfo.profile_picture = form.cleaned_data.get("profile_picture")
        new_user.cfo.bio = form.cleaned_data.get("bio")
        new_user.cfo.save()
    return super().form_valid(form)
