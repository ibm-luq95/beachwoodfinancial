# -*- coding: utf-8 -*-#
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

from client_account.filters import ClientAccountFilter
from client_account.forms import ClientAccountForm
from client_account.models import ClientAccount
from core.cache import BWCacheViewMixin
from core.utils import get_trans_txt
from core.views.mixins import BWBaseListViewMixin, BWLoginRequiredMixin


class ClientAccountListViewBW(
    BWLoginRequiredMixin,
    PermissionRequiredMixin,
    BWCacheViewMixin,
    BWBaseListViewMixin,
    ListView,
):
    template_name = "client_account/list.html"
    model = ClientAccount
    permission_required = ["client_account.can_view_list"]
    permission_denied_message = _("You do not have permission to access this page.")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Client Accounts"))
        context.setdefault("filter_form", self.filterset.form)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ClientAccountFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs


class ClientAccountCreateView(
    BWLoginRequiredMixin,
    PermissionRequiredMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    CreateView,
):
    template_name = "client_account/create.html"
    form_class = ClientAccountForm
    model = ClientAccount
    success_message = _("Contact created successfully")
    success_url = reverse_lazy("dashboard:client_account:list")
    permission_required = ["client_account.add_clientaccount"]
    permission_denied_message = _("You do not have permission to access this page.")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Create account"))
        messages.set_level(self.request, messages.DEBUG)
        return context


class ClientAccountUpdateView(
    BWLoginRequiredMixin,
    PermissionRequiredMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    UpdateView,
):
    template_name = "client_account/update.html"
    form_class = ClientAccountForm
    model = ClientAccount
    success_message = _("Contact updated successfully")
    success_url = reverse_lazy("dashboard:client_account:list")
    permission_required = ["client_account.change_clientaccount"]
    permission_denied_message = _("You do not have permission to access this page.")

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
    BWLoginRequiredMixin,
    PermissionRequiredMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    DeleteView,
):
    template_name = "client_account/delete.html"
    # form_class = ClientCategoryForm
    model = ClientAccount
    success_message = _("Contact deleted successfully")
    success_url = reverse_lazy("dashboard:client_account:list")
    permission_required = ["client_account.delete_clientaccount"]
    permission_denied_message = _("You do not have permission to access this page.")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Delete account"))
        return context
