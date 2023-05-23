# -*- coding: utf-8 -*-#
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic import CreateView

from client_category.forms import ClientCategoryForm
from client_category.models import ClientCategory
from core.utils import get_trans_txt


class ClientCategoryListView(TemplateView):
    template_name = "client_category/list.html.jinja"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Client Categories"))
        messages.set_level(self.request, messages.DEBUG)
        return context


class ClientCategoryCreateView(CreateView):
    template_name = "client_category/create.html.jinja"
    form_class = ClientCategoryForm
    model = ClientCategory

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Create client category"))
        messages.set_level(self.request, messages.DEBUG)
        return context
