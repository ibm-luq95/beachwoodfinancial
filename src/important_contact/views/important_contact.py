# -*- coding: utf-8 -*-#
from __future__ import annotations

from typing import Any

from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import QuerySet
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from core.cache import BWSiteSettingsViewMixin
from core.constants.css_classes import BW_INFO_MODAL_CSS_CLASSES
from core.constants.users import (
    CON_ASSISTANT,
    CON_BOOKKEEPER,
    CON_CFO,
    CON_MANAGER,
)
from core.utils import get_trans_txt
from core.views.mixins import (
    BWBaseListViewMixin,
    BWLoginRequiredMixin,
    BWObjectAccessRequiredMixin,
)
from core.views.mixins.update_previous_mixin import UpdateReturnPreviousMixin
from important_contact.filters import ImportantContactFilter
from important_contact.forms import ImportantContactForm
from important_contact.models import ImportantContact


class ImportantContactListViewBW(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWSiteSettingsViewMixin,
    BWBaseListViewMixin,
    ListView,
):
    template_name = "core/crudl/list.html"
    model = ImportantContact
    permission_required = "important_contact.can_view_list"
    permission_denied_message = _("You do not have permission to access this page.")

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Client contacts"))
        context.setdefault("filter_form", self.filterset.form)
        context.setdefault("page_header", _("contacts".capitalize()))
        context.setdefault(
            "component_path", "bw_components/important_contact/table_list.html"
        )
        context.setdefault("subtitle", _("contacts".title()))
        context.setdefault("actions_base_url", "dashboard:important_contact")
        context.setdefault("filter_cancel_url", "dashboard:important_contact:list")
        context.setdefault("table_header_title", _("C"))
        context.setdefault("table_header_subtitle", _("important_contact subtitle"))
        context.setdefault("is_show_create_btn", True)
        context.setdefault(
            "pagination_list_url_name", "dashboard:important_contact:list"
        )
        context.setdefault("is_filters_enabled", True)
        context.setdefault("is_actions_menu_enabled", True)
        context.setdefault("is_header_enabled", True)
        context.setdefault("is_footer_enabled", True)
        context.setdefault("actions_items", "update,delete")
        context.setdefault("base_url_name", "dashboard:important_contact")
        context.setdefault("empty_label", _("contacts"))
        context.setdefault("extra_context", {})
        context.setdefault("show_info_icon", True)
        context.setdefault(
            "info_details",
            {
                "tooltip_txt": BW_INFO_MODAL_CSS_CLASSES.get("important_contact").get(
                    "tooltip_txt"
                ),
                "modal_css_id": BW_INFO_MODAL_CSS_CLASSES.get(
                    "important_contact"
                ).get("cssID"),
            },
        )
        context.setdefault("filter_form_id", "importantContactFilterForm")
        if self.request.GET:
            context["title"] = _("Filtered Client contacts")
        else:
            context["title"] = _("Client contacts")
        return context

    def get_queryset(self) -> QuerySet[ImportantContact]:
        current_user = self.request.user
        if (
            current_user.user_type in (CON_MANAGER, CON_ASSISTANT)
            or current_user.is_superuser
        ):
            queryset = super().get_queryset()
        elif current_user.user_type == CON_BOOKKEEPER:
            bookkeeper_clients = (
                current_user.bookkeeper.get_proxy_model().clients.all()
            )
            if bookkeeper_clients:
                queryset = ImportantContact.objects.filter(
                    client__in=bookkeeper_clients
                )
            else:
                queryset = ImportantContact.objects.none()
        elif current_user.user_type == CON_CFO:
            cfo_clients = current_user.cfo.get_proxy_model().clients.all()
            if cfo_clients:
                queryset = ImportantContact.objects.filter(client__in=cfo_clients)
            else:
                queryset = ImportantContact.objects.none()
        else:
            queryset = ImportantContact.objects.none()

        self.filterset = ImportantContactFilter(
            self.request.GET, queryset=queryset
        )
        return self.filterset.qs


class ImportantContactCreateView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWSiteSettingsViewMixin,
    BWBaseListViewMixin,
    SuccessMessageMixin,
    CreateView,
):
    permission_required = "important_contact.add_importantcontact"
    permission_denied_message = _("You do not have permission to access this page.")
    template_name = "important_contact/create.html"
    form_class = ImportantContactForm
    model = ImportantContact
    success_message = _("Contact created successfully")
    success_url = reverse_lazy("dashboard:important_contact:list")

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Create contact"))
        messages.set_level(self.request, messages.DEBUG)
        return context


class ImportantContactUpdateView(
    PermissionRequiredMixin,
    BWObjectAccessRequiredMixin,
    BWLoginRequiredMixin,
    BWSiteSettingsViewMixin,
    SuccessMessageMixin,
    UpdateReturnPreviousMixin,
    UpdateView,
):
    template_name = "important_contact/update.html"
    permission_required = "important_contact.change_importantcontact"
    permission_denied_message = _("You do not have permission to access this page.")
    form_class = ImportantContactForm
    model = ImportantContact
    success_message = _("Contact updated successfully")
    BASE_SUCCESS_URL = "dashboard:important_contact:list"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Update contact"))
        messages.set_level(self.request, messages.DEBUG)
        return context


class ImportantContactDeleteView(
    PermissionRequiredMixin,
    BWObjectAccessRequiredMixin,
    BWLoginRequiredMixin,
    BWSiteSettingsViewMixin,
    SuccessMessageMixin,
    DeleteView,
):
    template_name = "core/crudl/delete.html"
    permission_required = "important_contact.delete_importantcontact"
    permission_denied_message = _("You do not have permission to access this page.")
    model = ImportantContact
    success_message = _("Contact deleted successfully")
    success_url = reverse_lazy("dashboard:important_contact:list")

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Delete contact"))
        context.setdefault("cancel_url", "dashboard:important_contact:list")
        context.setdefault("object", self.get_object())
        context.setdefault("object_name", "client contact")
        context.setdefault("form_css_id", "importantContactDeleteForm")
        return context
