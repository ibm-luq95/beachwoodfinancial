# -*- coding: utf-8 -*-#
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

from client_category.filters import ClientCategoryFilter
from client_category.forms import ClientCategoryForm
from client_category.models import ClientCategory
from core.utils import get_trans_txt, debugging_print
from core.views.mixins import BaseListViewMixin


class ClientCategoryListView(BaseListViewMixin, ListView):
    template_name = "client_category/list.html"
    model = ClientCategory

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


class ClientCategoryCreateView(SuccessMessageMixin, CreateView):
    template_name = "client_category/create.html"
    form_class = ClientCategoryForm
    model = ClientCategory
    success_message = _("Category created successfully")
    success_url = reverse_lazy("dashboard:client_category:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Create client category"))
        messages.set_level(self.request, messages.DEBUG)
        return context


class ClientCategoryUpdateView(SuccessMessageMixin, UpdateView):
    template_name = "client_category/update.html"
    form_class = ClientCategoryForm
    model = ClientCategory
    success_message = _("Category updated successfully")
    success_url = reverse_lazy("dashboard:client_category:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Update client category"))
        messages.set_level(self.request, messages.DEBUG)
        return context


class ClientCategoryDeleteView(SuccessMessageMixin, DeleteView):
    template_name = "client_category/delete.html"
    # form_class = ClientCategoryForm
    model = ClientCategory
    success_message = _("Category deleted successfully")
    success_url = reverse_lazy("dashboard:client_category:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Delete client category"))
        return context
