# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from core.cache import BWCacheViewMixin
from core.constants import LIST_VIEW_PAGINATE_BY
from core.constants.users import CON_BOOKKEEPER
from core.views.mixins import BWBaseListViewMixin, BWLoginRequiredMixin
from document.filters import DocumentFilter
from document.forms import DocumentForm
from document.models import Document


# from documents.forms import DocumentForm


# from jobs.forms import JobForm
# from manager.views.mixins import BWManagerAccessMixin, ManagerAssistantAccessMixin
# from notes.forms import NoteForm
# from special_assignment.forms import SpecialAssignmentForm
# from task.forms import TaskForm


class DocumentListView(
    BWLoginRequiredMixin,
    PermissionRequiredMixin,
    BWCacheViewMixin,
    BWBaseListViewMixin,
    ListView,
):
    permission_required = ["document.can_view_list"]
    permission_denied_message = _("You do not have permission to access this page.")
    template_name = "document/list.html"
    model = Document
    # queryset = Client.objects.filter(~Q(status="archive")).prefetch_related("jobs")
    # queryset = Client.objects.prefetch_related(
    #     "jobs", "jobs__created_by", "important_contacts"
    # ).filter(~Q(status=CON_ARCHIVED))
    paginate_by = LIST_VIEW_PAGINATE_BY
    list_type = "list"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = _("Documents")
        context.setdefault("filter_form", self.filterset.form)
        context.setdefault("list_type", self.list_type)
        context.setdefault("page_header", "documents".title())

        # debugging_print(self.filterset.form["name"])
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.user_type == CON_BOOKKEEPER:
            queryset = (
                self.request.user.bookkeeper.get_proxy_model().get_all_related_items(
                    "documents"
                )
            )
        self.filterset = DocumentFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs


class DocumentCreateView(
    BWLoginRequiredMixin,
    PermissionRequiredMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    CreateView,
):
    permission_required = ["document.add_document"]
    permission_denied_message = _("You do not have permission to access this page.")
    template_name = "document/create.html"
    form_class = DocumentForm
    success_message = _("Document created successfully")
    success_url = reverse_lazy("dashboard:document:list")

    # template_name_suffix = "_create_client"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Create document"))
        return context

    # def form_valid(self, form: BaseForm):
    #     debugging_print(form.cleaned_data)
    #     return super().form_valid(form)
    #
    # def form_invalid(self, form):
    #     """If the form is invalid, render the invalid form."""
    #     debugging_print(form.cleaned_data)
    #     return self.render_to_response(self.get_context_data(form=form))


class DocumentUpdateView(
    BWLoginRequiredMixin,
    PermissionRequiredMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    UpdateView,
):
    permission_required = ["document.change_document"]
    permission_denied_message = _("You do not have permission to access this page.")
    template_name = "document/update.html"
    form_class = DocumentForm
    success_message = _("Document updated successfully")
    success_url = reverse_lazy("dashboard:document:list")
    model = Document

    # template_name_suffix = "_create_client"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Update document"))
        return context

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super().get_form_kwargs()
        # sections = ["job", "client", "task"]
        object = self.get_object()
        # for sec in sections:
        #     if sec == object.document_section:
        #         sections.remove(sec)
        # kwargs.update({"is_update": True, "removed_fields": sections})
        kwargs.update({"is_update": True})
        return kwargs


class DocumentDeleteView(
    BWLoginRequiredMixin,
    PermissionRequiredMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    DeleteView,
):
    permission_required = ["document.delete_document"]
    permission_denied_message = _("You do not have permission to access this page.")
    template_name = "document/delete.html"
    model = Document
    success_message = _("Document deleted successfully")
    success_url = reverse_lazy("dashboard:document:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Delete document"))
        return context
