# -*- coding: utf-8 -*-#
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

from important_contact.filters import ImportantContactFilter
from important_contact.forms import ImportantContactForm
from important_contact.models import ImportantContact
from core.utils import get_trans_txt, debugging_print
from core.views.mixins import BaseListViewMixin


class ImportantContactListView(BaseListViewMixin, ListView):
    template_name = "important_contact/list.html"
    model = ImportantContact

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Client Categories"))
        context.setdefault("filter_form", self.filterset.form)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ImportantContactFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs


class ImportantContactCreateView(SuccessMessageMixin, CreateView):
    template_name = "important_contact/create.html"
    form_class = ImportantContactForm
    model = ImportantContact
    success_message = _("Contact created successfully")
    success_url = reverse_lazy("dashboard:important_contact:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Create contact"))
        messages.set_level(self.request, messages.DEBUG)
        return context


class ImportantContactUpdateView(SuccessMessageMixin, UpdateView):
    template_name = "important_contact/update.html"
    form_class = ImportantContactForm
    model = ImportantContact
    success_message = _("Contact updated successfully")
    success_url = reverse_lazy("dashboard:important_contact:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Update contact"))
        messages.set_level(self.request, messages.DEBUG)
        return context


class ImportantContactDeleteView(SuccessMessageMixin, DeleteView):
    template_name = "important_contact/delete.html"
    # form_class = ClientCategoryForm
    model = ImportantContact
    success_message = _("Contact deleted successfully")
    success_url = reverse_lazy("dashboard:important_contact:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Delete contact"))
        return context
