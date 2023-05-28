# -*- coding: utf-8 -*-#
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView
from django.views.generic import ListView

from client_category.forms import ClientCategoryForm
from client_category.models import ClientCategory
from core.utils import get_trans_txt
from core.views.mixins import BaseListViewMixin


class ClientCategoryListView(BaseListViewMixin, ListView):
    template_name = "client_category/list.html"
    model = ClientCategory

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Client Categories"))
        context.setdefault("table_header_columns", self.model.get_columns_names())
        # debugging_print(self.model.get_columns_names())
        messages.set_level(self.request, messages.DEBUG)
        return context


class ClientCategoryCreateView(SuccessMessageMixin, CreateView):
    template_name = "client_category/create.html"
    form_class = ClientCategoryForm
    model = ClientCategory
    success_message = _("Category created successfully")
    success_url = reverse_lazy("dashboard:client_category:create")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Create client category"))
        messages.set_level(self.request, messages.DEBUG)
        return context
