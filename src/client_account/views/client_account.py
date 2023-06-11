# -*- coding: utf-8 -*-#
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

from client_account.filters import ClientAccountFilter
from client_account.forms import ClientAccountForm
from client_account.models import ClientAccount
from core.cache import BWCacheViewMixin

from core.utils import get_trans_txt, debugging_print
from core.views.mixins import (
    BWBaseListViewMixin,
    BWLoginRequiredMixin,
    BWManagerAccessMixin,
)


class ClientAccountListViewBW(
    BWLoginRequiredMixin,
    BWManagerAccessMixin,
    BWCacheViewMixin,
    BWBaseListViewMixin,
    ListView,
):
    template_name = "client_account/list.html"
    model = ClientAccount

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
    BWManagerAccessMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    CreateView,
):
    template_name = "client_account/create.html"
    form_class = ClientAccountForm
    model = ClientAccount
    success_message = _("Contact created successfully")
    success_url = reverse_lazy("dashboard:client_account:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Create account"))
        messages.set_level(self.request, messages.DEBUG)
        return context


class ClientAccountUpdateView(
    BWLoginRequiredMixin,
    BWManagerAccessMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    UpdateView,
):
    template_name = "client_account/update.html"
    form_class = ClientAccountForm
    model = ClientAccount
    success_message = _("Contact updated successfully")
    success_url = reverse_lazy("dashboard:client_account:list")

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
    BWManagerAccessMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    DeleteView,
):
    template_name = "client_account/delete.html"
    # form_class = ClientCategoryForm
    model = ClientAccount
    success_message = _("Contact deleted successfully")
    success_url = reverse_lazy("dashboard:client_account:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Delete account"))
        return context
