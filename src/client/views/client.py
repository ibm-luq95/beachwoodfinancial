# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
    RedirectView,
    FormView,
)
from django.utils.translation import gettext as _

from bookkeeper.models import BookkeeperProxy
from client.filters import ClientFilter
from client.forms import ClientForm, ClientMiniForm
from client.models import ClientProxy
from client_account.forms import ClientAccountForm
from core.cache import BWCacheViewMixin
from core.config.forms import BWFormRenderer
from core.constants import LIST_VIEW_PAGINATE_BY
from core.constants.status_labels import CON_ARCHIVED, CON_ENABLED
from core.utils import get_trans_txt, debugging_print
from core.views.mixins import (
    BWBaseListViewMixin,
    BWLoginRequiredMixin,
    BWListViewMixin,
    BWArchiveListViewMixin,
    BWManagerAccessMixin,
)
from document.forms import DocumentForm

# from documents.forms import DocumentForm
from important_contact.forms import ImportantContactForm, ImportantContactMiniForm
from job.forms import JobForm, JobMiniForm
from note.forms import NoteForm
from special_assignment.forms import MiniSpecialAssignmentForm
from task.forms import TaskForm


# from jobs.forms import JobForm
# from manager.views.mixins import BWManagerAccessMixin, ManagerAssistantAccessMixin
# from notes.forms import NoteForm
# from special_assignment.forms import SpecialAssignmentForm
# from task.forms import TaskForm


class ClientListView(
    BWLoginRequiredMixin,
    BWManagerAccessMixin,
    BWCacheViewMixin,
    BWBaseListViewMixin,
    ListView,
):
    # permission_required = "client.can_view_list"
    template_name = "client/list.html"
    model = ClientProxy
    # queryset = Client.objects.filter(~Q(status="archive")).prefetch_related("jobs")
    # queryset = Client.objects.prefetch_related(
    #     "jobs", "jobs__created_by", "important_contacts"
    # ).filter(~Q(status=CON_ARCHIVED))
    paginate_by = LIST_VIEW_PAGINATE_BY
    list_type = "list"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = _("Clients")
        context.setdefault("filter_form", self.filterset.form)
        context.setdefault("list_type", self.list_type)
        context.setdefault("page_header", "clients".title())

        # debugging_print(self.filterset.form["name"])
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        # if self.request.user.user_type == "bookkeeper":
        #     queryset = BookkeeperProxy.objects.get(
        #         pk=self.request.user.bookkeeper.pk
        #     ).clients.all()
        self.filterset = ClientFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs


class ClientCreateView(
    BWLoginRequiredMixin,
    BWManagerAccessMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    CreateView,
):
    # permission_required = "client.add_client"
    template_name = "client/create.html"
    form_class = ClientForm
    success_message = _("Client created successfully")
    success_url = reverse_lazy("dashboard:client:list")

    # template_name_suffix = "_create_client"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Create client"))
        return context

    # def form_valid(self, form: BaseForm):
    #     debugging_print(form.cleaned_data)
    #     return super().form_valid(form)


class ClientUpdateView(
    BWLoginRequiredMixin,
    BWManagerAccessMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    UpdateView,
):
    # permission_required = "client.add_client"
    template_name = "client/update.html"
    form_class = ClientForm
    success_message = _("Client updated successfully")
    success_url = reverse_lazy("dashboard:client:list")
    model = ClientProxy

    # template_name_suffix = "_create_client"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Update client"))
        return context

    # def form_valid(self, form: BaseForm):
    #     debugging_print(form.cleaned_data)
    #     return super().form_valid(form)


class ClientDeleteView(
    BWLoginRequiredMixin,
    BWManagerAccessMixin,
    BWCacheViewMixin,
    BWBaseListViewMixin,
    SuccessMessageMixin,
    DeleteView,
):
    template_name = "client/delete.html"
    # form_class = ClientCategoryForm
    model = ClientProxy
    success_message = _("Client deleted successfully")
    success_url = reverse_lazy("dashboard:client:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Delete client"))
        return context


class ClientDetailsView(
    BWLoginRequiredMixin, BWManagerAccessMixin, BWCacheViewMixin, DetailView
):
    template_name = "client/details.html"
    # form_class = ClientCategoryForm
    model = ClientProxy

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Client details"))
        job_form = JobMiniForm(initial={"client": self.get_object().pk})
        important_contact_form = ImportantContactForm(
            initial={"client": self.get_object()}, renderer=BWFormRenderer()
        )
        client_form = ClientForm(
            instance=self.get_object(),
            renderer=BWFormRenderer(),
            removed_fields=["categories", "bookkeepers", "important_contacts", "status"],
        )
        client_mini_form = ClientMiniForm()
        task_form = TaskForm(
            initial={"client": self.get_object()},
            # removed_fields=["job"],
            hidden_fields=["job"],
            renderer=BWFormRenderer(),
        )
        document_form = DocumentForm(
            initial={"client": self.get_object(), "document_section": "client"},
            renderer=BWFormRenderer(),
            removed_fields=["task", "status", "job", "document_section"],
            hidden_inputs={"field_names": ["client"]},
        )
        note_form = NoteForm(
            renderer=BWFormRenderer(),
            initial={"client": self.get_object()},
            removed_fields=["task", "job"],
            hidden_inputs={"field_names": ["client"]}
        )
        special_assignment_form = MiniSpecialAssignmentForm(
            renderer=BWFormRenderer(),
            initial={"assigned_by": self.request.user.pk, "client": self.get_object().pk},
        )
        client_account_form = ClientAccountForm(
            initial={"client": self.get_object(), "status": CON_ENABLED},
            renderer=BWFormRenderer(),
            hidden_inputs={"field_names": ["client", "status"]},
        )
        context.setdefault("job_form", job_form)
        # context.setdefault("job_status_choices", JobStatusEnum.choices)
        context.setdefault("task_form", task_form)
        context.setdefault("document_form", document_form)
        context.setdefault("client_form", client_form)
        context.setdefault("important_contact_form", important_contact_form)
        context.setdefault("note_form", note_form)
        context.setdefault("client_mini_form", client_mini_form)
        context.setdefault("special_assignment_form", special_assignment_form)
        context.setdefault("client_account_form", client_account_form)
        return context
