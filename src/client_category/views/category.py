# -*- coding: utf-8 -*-#
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

from client_category.filters import ClientCategoryFilter
from client_category.forms import ClientCategoryForm
from client_category.models import ClientCategory
from core.cache import BWCacheViewMixin
from core.utils import get_trans_txt
from core.views.mixins import BWBaseListViewMixin, BWLoginRequiredMixin


class ClientCategoryListViewBW(
    BWLoginRequiredMixin,
    PermissionRequiredMixin,
    BWCacheViewMixin,
    BWBaseListViewMixin,
    ListView,
):
    template_name = "client_category/list.html"
    model = ClientCategory
    permission_required = ["client_category.can_view_list"]
    permission_denied_message = _("You do not have permission to access this page.")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Client Categories"))
        context.setdefault("filter_form", self.filterset.form)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ClientCategoryFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs


class ClientCategoryCreateView(
    BWLoginRequiredMixin,
    PermissionRequiredMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    CreateView,
):
    template_name = "client_category/create.html"
    form_class = ClientCategoryForm
    model = ClientCategory
    success_message = _("Category created successfully")
    success_url = reverse_lazy("dashboard:client_category:list")
    permission_required = ["client_category.add_clientcategory"]
    permission_denied_message = _("You do not have permission to access this page.")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Create client category"))
        messages.set_level(self.request, messages.DEBUG)
        return context


class ClientCategoryUpdateView(
    BWLoginRequiredMixin,
    PermissionRequiredMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    UpdateView,
):
    template_name = "client_category/update.html"
    form_class = ClientCategoryForm
    model = ClientCategory
    success_message = _("Category updated successfully")
    success_url = reverse_lazy("dashboard:client_category:list")
    permissions_required = ["client_category.change_clientcategory"]
    permission_denied_message = _("You do not have permission to access this page.")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Update client category"))
        messages.set_level(self.request, messages.DEBUG)
        return context


class ClientCategoryDeleteView(
    BWLoginRequiredMixin,
    PermissionRequiredMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    DeleteView,
):
    template_name = "client_category/delete.html"
    model = ClientCategory
    success_message = _("Category deleted successfully")
    success_url = reverse_lazy("dashboard:client_category:list")
    permissions_required = ["client_category.delete_clientcategory"]
    permission_denied_message = _("You do not have permission to access this page.")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Delete client category"))
        return context
