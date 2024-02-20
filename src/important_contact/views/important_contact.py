# -*- coding: utf-8 -*-#
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import UpdateView

from core.cache import BWCacheViewMixin
from core.constants.css_classes import BW_INFO_MODAL_CSS_CLASSES
from core.constants.users import CON_ASSISTANT
from core.constants.users import CON_BOOKKEEPER
from core.constants.users import CON_MANAGER
from core.utils import get_trans_txt
from core.views.mixins import BWBaseListViewMixin
from core.views.mixins import BWLoginRequiredMixin
from core.views.mixins.update_previous_mixin import UpdateReturnPreviousMixin
from important_contact.filters import ImportantContactFilter
from important_contact.forms import ImportantContactForm
from important_contact.models import ImportantContact


class ImportantContactListViewBW(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWCacheViewMixin,
    BWBaseListViewMixin,
    ListView,
):
    permission_required = "important_contact.can_view_list"
    permission_denied_message = _("You do not have permission to access this page.")
    template_name = "core/crudl/list.html"
    model = ImportantContact

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Client Contacts"))
        context.setdefault("filter_form", self.filterset.form)
        context.setdefault("page_header", _("contacts".capitalize()))
        context.setdefault(
            "component_path", "bw_components/important_contact/table_list.html"
        )
        context.setdefault("subtitle", _("Client contacts".title()))
        context.setdefault("actions_base_url", "dashboard:important_contact")
        context.setdefault("filter_cancel_url", "dashboard:important_contact:list")
        context.setdefault("table_header_title", _("C"))
        context.setdefault("table_header_subtitle", _("important_contact subtitle"))
        context.setdefault("is_show_create_btn", True)
        context.setdefault("pagination_list_url_name", "dashboard:important_contact:list")
        context.setdefault("is_filters_enabled", True)
        context.setdefault("is_actions_menu_enabled", True)
        context.setdefault("is_header_enabled", True)
        context.setdefault("is_footer_enabled", True)
        context.setdefault("actions_items", "update,delete")
        context.setdefault("base_url_name", "dashboard:important_contact")
        context.setdefault("empty_label", _("contacts"))
        context.setdefault("extra_context", {"is_client_enabled": True})
        context.setdefault("show_info_icon", True)
        context.setdefault(
            "info_details",
            {
                "tooltip_txt": BW_INFO_MODAL_CSS_CLASSES.get("important_contact").get(
                    "tooltip_txt"
                ),
                "modal_css_id": BW_INFO_MODAL_CSS_CLASSES.get("important_contact").get(
                    "cssID"
                ),
            },
        )
        return context

    def get_queryset(self):

        current_user = self.request.user
        if (
            current_user.user_type == CON_MANAGER
            or current_user.user_type == CON_ASSISTANT
        ):
            queryset = super().get_queryset()
        elif current_user.user_type == CON_BOOKKEEPER:
            bookkeeper_clients = current_user.bookkeeper.get_proxy_model().clients.all()
            if bookkeeper_clients:
                queryset = ImportantContact.objects.filter(client__in=bookkeeper_clients)
            else:
                queryset = ImportantContact.objects.none()

        self.filterset = ImportantContactFilter(self.request.GET, queryset=queryset)

        return self.filterset.qs


class ImportantContactCreateView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWCacheViewMixin,
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

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Create contact"))
        messages.set_level(self.request, messages.DEBUG)
        return context


class ImportantContactUpdateView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWCacheViewMixin,
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

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Update contact"))
        messages.set_level(self.request, messages.DEBUG)
        return context


class ImportantContactDeleteView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    DeleteView,
):
    template_name = "core/crudl/delete.html"
    permission_required = "important_contact.delete_importantcontact"
    permission_denied_message = _("You do not have permission to access this page.")
    model = ImportantContact
    success_message = _("Contact deleted successfully")
    success_url = reverse_lazy("dashboard:important_contact:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Delete contact"))
        context.setdefault("cancel_url", "dashboard:important_contact:list")
        context.setdefault("object", self.get_object())
        context.setdefault("object_name", "client contact")
        context.setdefault("form_css_id", "importantContactDeleteForm")
        return context
