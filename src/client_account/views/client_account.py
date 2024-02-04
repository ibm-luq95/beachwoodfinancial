# -*- coding: utf-8 -*-#
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import QuerySet
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

from client_account.filters import ClientAccountFilter
from client_account.forms import ClientAccountForm
from client_account.models import ClientAccount
from core.cache import BWCacheViewMixin
from core.constants.css_classes import BW_INFO_MODAL_CSS_CLASSES
from core.constants.users import CON_BOOKKEEPER
from core.utils import get_trans_txt
from core.views.mixins import BWBaseListViewMixin, BWLoginRequiredMixin
from core.views.mixins.update_previous_mixin import UpdateReturnPreviousMixin


class ClientAccountListViewBW(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWCacheViewMixin,
    BWBaseListViewMixin,
    ListView,
):
    template_name = "core/crudl/list.html"
    model = ClientAccount
    permission_required = "client_account.can_view_list"
    permission_denied_message = _("You do not have permission to access this page.")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Client Accounts"))
        context.setdefault("filter_form", self.filterset.form)
        context.setdefault("page_header", _("client accounts".capitalize()))
        context.setdefault(
            "component_path", "bw_components/client_account/table_list.html"
        )
        context.setdefault("subtitle", _("client accounts".title()))
        context.setdefault("actions_base_url", "dashboard:client_account")
        context.setdefault("filter_cancel_url", "dashboard:client_account:list")
        context.setdefault("table_header_title", _("C"))
        context.setdefault("table_header_subtitle", _("client_account subtitle"))
        context.setdefault("is_show_create_btn", True)
        context.setdefault("pagination_list_url_name", "dashboard:client_account:list")
        context.setdefault("is_filters_enabled", True)
        context.setdefault("is_actions_menu_enabled", True)
        context.setdefault("is_header_enabled", True)
        context.setdefault("is_footer_enabled", True)
        context.setdefault("actions_items", "update,delete")
        context.setdefault("base_url_name", "dashboard:client_account")
        context.setdefault("empty_label", _("accounts"))
        context.setdefault("extra_context", {})
        context.setdefault("show_info_icon", True)
        context.setdefault(
            "info_details",
            {
                "tooltip_txt": BW_INFO_MODAL_CSS_CLASSES.get("client_account").get(
                    "tooltip_txt"
                ),
                "modal_css_id": BW_INFO_MODAL_CSS_CLASSES.get("client_account").get(
                    "cssID"
                ),
            },
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.user_type == CON_BOOKKEEPER:
            clients = self.request.user.bookkeeper.get_proxy_model().clients.all()
            services = ClientAccount.objects.none()
            for client in clients:
                services |= client.client_accounts.all()
            qs = services
        else:
            qs = queryset
        self.filterset = ClientAccountFilter(self.request.GET, queryset=qs)
        return self.filterset.qs


class ClientAccountCreateView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    CreateView,
):
    template_name = "client_account/create.html"
    form_class = ClientAccountForm
    model = ClientAccount
    success_message = _("Client account created successfully")
    success_url = reverse_lazy("dashboard:client_account:list")
    permission_required = "client_account.add_clientaccount"
    permission_denied_message = _("You do not have permission to access this page.")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Create account"))
        messages.set_level(self.request, messages.DEBUG)
        return context


class ClientAccountUpdateView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    UpdateReturnPreviousMixin,
    UpdateView,
):
    template_name = "client_account/update.html"
    form_class = ClientAccountForm
    model = ClientAccount
    success_message = _("Contact updated successfully")
    permission_required = "client_account.change_clientaccount"
    permission_denied_message = _("You do not have permission to access this page.")
    BASE_SUCCESS_URL = "dashboard:client_account:list"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Update account"))
        messages.set_level(self.request, messages.DEBUG)
        return context

    def get_form_kwargs(self):
        kwargs = super(ClientAccountUpdateView, self).get_form_kwargs()
        kwargs.update({"is_update": True, "updated_object": self.get_object()})
        return kwargs


class ClientAccountDeleteView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    DeleteView,
):
    template_name = "core/crudl/delete.html"
    # form_class = ClientCategoryForm
    model = ClientAccount
    success_message = _("Contact deleted successfully")
    success_url = reverse_lazy("dashboard:client_account:list")
    permission_required = "client_account.delete_clientaccount"
    permission_denied_message = _("You do not have permission to access this page.")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Delete account"))
        context.setdefault("cancel_url", "dashboard:client_account:list")
        context.setdefault("object", self.get_object())
        context.setdefault("object_name", "client account")
        context.setdefault("form_css_id", "clientAccountDeleteForm")
        return context
