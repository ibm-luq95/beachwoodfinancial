# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.forms import BaseForm
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
from client.forms import ClientForm
from client.models import ClientProxy
from core.constants import LIST_VIEW_PAGINATE_BY
from core.constants.status_labels import CON_ARCHIVED
from core.utils import get_trans_txt, debugging_print
from core.views.mixins import (
    BWBaseListViewMixin,
    BWLoginRequiredMixin,
    BWListViewMixin,
    BWArchiveListViewMixin,
)

# from documents.forms import DocumentForm
from important_contact.forms import ImportantContactForm


# from jobs.forms import JobForm
# from manager.views.mixins import BWManagerAccessMixin, ManagerAssistantAccessMixin
# from notes.forms import NoteForm
# from special_assignment.forms import SpecialAssignmentForm
# from task.forms import TaskForm


class ClientListViewBW(BWBaseListViewMixin, ListView):
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


class ClientCreateView(SuccessMessageMixin, CreateView):
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
