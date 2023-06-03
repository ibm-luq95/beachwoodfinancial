# -*- coding: utf-8 -*-#
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView
from django.views.generic import ListView

from client_category.forms import ClientCategoryForm
from client_category.models import ClientCategory
from core.utils import get_trans_txt, debugging_print
from core.views.mixins import BaseListViewMixin
from django_tables2 import tables
from django_tables2 import SingleTableView


class PersonTable(tables.Table):
    class Meta:
        model = ClientCategory
        # template_name = "bw_ui_components/django_tables2/base_table.html"
        # fields = ("name", "created_at")
        exclude = ("id", "updated_at", "is_deleted", "metadata", "deleted_at")
        sequence = ["name", "status", "created_at"]


# class ClientCategoryListView(SingleTableView):
#     model = ClientCategory
#     table_class = PersonTable
#     template_name = "client_category/list.html"


class ClientCategoryListView(BaseListViewMixin, ListView):
    template_name = "client_category/list.html"
    model = ClientCategory

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Client Categories"))
        context.setdefault("table_header_columns", self.model.get_columns_names())
        context.setdefault("table_headers", ["name", "clients", "created"])
        # debugging_print(self.object_list.values())
        # debugging_print(type(self.object_list.values()))
        object_new_list = list()
        for obj in self.object_list:
            data_dict = dict()
            data_dict.update(
                {"name": obj.name, "status": obj.get_status_display(), "clients": 5}
            )
            if context.get("is_show_created_at") is True:
                data_dict.update({"created": obj.created_at})
            object_new_list.append(data_dict)
        context.setdefault("object_new_list", object_new_list)
        debugging_print(object_new_list)
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
