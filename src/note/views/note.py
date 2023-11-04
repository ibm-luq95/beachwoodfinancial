# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from core.cache import BWCacheViewMixin
from core.constants import LIST_VIEW_PAGINATE_BY
from core.constants.css_classes import BW_INFO_MODAL_CSS_CLASSES
from core.constants.users import CON_BOOKKEEPER
from core.views.mixins import BWLoginRequiredMixin, BWBaseListViewMixin
from core.views.mixins.bookkeeper_pass_related_mixin import BookkeeperPassRelatedMixin
from note.filters import NoteFilter
from note.forms import NoteForm
from note.models import Note


class NoteListView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWCacheViewMixin,
    BWBaseListViewMixin,
    ListView,
):
    permission_required = "note.can_view_list"
    permission_denied_message = _("You do not have permission to access this page.")
    template_name = "core/crudl/list.html"
    model = Note
    paginate_by = LIST_VIEW_PAGINATE_BY
    list_type = "list"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = _("Notes")
        context.setdefault("filter_form", self.filterset.form)
        context.setdefault("list_type", self.list_type)
        context.setdefault("page_header", _("notes".title()))
        context.setdefault("component_path", "bw_components/note/table_list.html")
        context.setdefault("subtitle", _("note".title()))
        context.setdefault("actions_base_url", "dashboard:note")
        context.setdefault("filter_cancel_url", "dashboard:note:list")
        context.setdefault("table_header_title", _("C"))
        context.setdefault("table_header_subtitle", _("notes subtitle"))
        context.setdefault("is_show_create_btn", True)
        context.setdefault("pagination_list_url_name", "dashboard:note:list")
        context.setdefault("is_filters_enabled", True)
        context.setdefault("is_actions_menu_enabled", True)
        context.setdefault("is_header_enabled", True)
        context.setdefault("is_footer_enabled", True)
        context.setdefault("actions_items", "update,delete")
        context.setdefault("base_url_name", "dashboard:note")
        context.setdefault("empty_label", _("notes"))
        context.setdefault("extra_context", {"is_show_section": True})
        context.setdefault("show_info_icon", True)
        context.setdefault(
            "info_details",
            {
                "tooltip_txt": BW_INFO_MODAL_CSS_CLASSES.get("note").get("tooltip_txt"),
                "modal_css_id": BW_INFO_MODAL_CSS_CLASSES.get("note").get("cssID"),
            },
        )

        # debugging_print(self.filterset.form["name"])
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.user_type == CON_BOOKKEEPER:
            queryset = (
                self.request.user.bookkeeper.get_proxy_model().get_all_related_items(
                    "notes"
                )
            )
        self.filterset = NoteFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs


class NoteCreateView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    BookkeeperPassRelatedMixin,
    CreateView,
):
    permission_required = "note.add_note"
    permission_denied_message = _("You do not have permission to access this page.")
    template_name = "note/create.html"
    form_class = NoteForm
    success_message = _("Note created successfully")
    success_url = reverse_lazy("dashboard:note:list")

    # template_name_suffix = "_create_client"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Create note"))
        return context


class NoteUpdateView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    BookkeeperPassRelatedMixin,
    UpdateView,
):
    permission_required = "note.change_note"
    permission_denied_message = _("You do not have permission to access this page.")
    template_name = "note/update.html"
    form_class = NoteForm
    success_message = _("Note updated successfully")
    success_url = reverse_lazy("dashboard:note:list")
    model = Note

    # template_name_suffix = "_create_client"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Update note"))
        return context


class NoteDeleteView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWCacheViewMixin,
    BWBaseListViewMixin,
    SuccessMessageMixin,
    DeleteView,
):
    template_name = "note/delete.html"
    permission_required = "note.delete_note"
    permission_denied_message = _("You do not have permission to access this page.")
    model = Note
    success_message = _("Note deleted successfully")
    success_url = reverse_lazy("dashboard:note:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Delete note"))
        return context
