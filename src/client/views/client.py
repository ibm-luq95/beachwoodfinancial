# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from client.filters import ClientFilter
from client.forms import ClientForm, ClientMiniForm, AssignBookkeeperForm
from client.models import ClientProxy
from client_account.forms import ClientAccountForm
from client_category.forms import ClientCategoryForm
from client_category.models import ClientCategory
from core.cache import BWCacheViewMixin
from core.config.forms import BWFormRenderer
from core.constants import LIST_VIEW_PAGINATE_BY
from core.constants.css_classes import BW_INFO_MODAL_CSS_CLASSES
from core.constants.status_labels import CON_ENABLED
from core.constants.users import CON_BOOKKEEPER, CON_MANAGER, CON_ASSISTANT
from core.utils.developments.debugging_print_object import BWDebuggingPrint
from core.views.mixins import BWBaseListViewMixin, BWLoginRequiredMixin
from core.views.mixins.base_list_view import BWSectionDescriptionHelperMixin
from document.forms import DocumentForm

# from documents.forms import DocumentForm
from important_contact.forms import ImportantContactForm
from job.forms import JobMiniForm
from note.forms import NoteForm
from special_assignment.forms import MiniSpecialAssignmentForm
from task.forms import TaskForm


class ClientListView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWCacheViewMixin,
    BWBaseListViewMixin,
    ListView,
):
    permission_required = "client.can_view_list"
    permission_denied_message = _("You do not have permission to access this page.")
    template_name = "core/crudl/list.html"
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
        context.setdefault("component_path", "bw_components/client/table_list.html")
        context.setdefault("filter_form", self.filterset.form)
        context.setdefault("list_type", self.list_type)
        context.setdefault("page_header", "client".title())
        context.setdefault("subtitle", "Clients".title())
        context.setdefault("actions_base_url", "dashboard:client")
        context.setdefault("filter_cancel_url", "dashboard:client:list")
        context.setdefault("table_header_title", _("C"))
        context.setdefault("table_header_subtitle", _("Client accounts for all services"))
        context.setdefault("is_show_create_btn", True)
        context.setdefault("pagination_list_url_name", "dashboard:client:list")
        context.setdefault("is_filters_enabled", True)
        context.setdefault("is_actions_menu_enabled", True)
        context.setdefault("is_header_enabled", True)
        context.setdefault("is_footer_enabled", True)
        context.setdefault("actions_items", "details,update,delete")
        context.setdefault("base_url_name", "dashboard:client")
        context.setdefault("empty_label", _("client"))
        context.setdefault("extra_context", {"is_show_bookkeeper": True})
        context.setdefault("show_info_icon", True)
        context.setdefault(
            "info_details",
            {
                "tooltip_txt": BW_INFO_MODAL_CSS_CLASSES.get("client").get("tooltip_txt"),
                "modal_css_id": BW_INFO_MODAL_CSS_CLASSES.get("client").get("cssID"),
            },
        )
        context.setdefault("filter_categories_is_enabled", True)
        context.setdefault(
            "filter_categories",
            {
                "categories_add_form": ClientCategoryForm,
                "categories_add_form_css_id": "clientCategoriesCreateForm",
                "categories_object_list": ClientCategory.objects.all(),
                "categories_add_form_css_class": "filterCategoryForms",
                "categories_modal_title": _("Client categories"),
                "category_app_label": "client_category",
                "category_filter_form_action_url": reverse_lazy(
                    "dashboard:client_category:api:client-category-api-router-list"
                ),
                "is_actions_menu_enabled": False,
            },
        )

        # debugging_print(self.filterset.form["name"])
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.user_type == CON_BOOKKEEPER:
            queryset = self.request.user.bookkeeper.get_proxy_model().clients.all()
        self.filterset = ClientFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs


class ClientCreateView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    CreateView,
):
    # permission_required = ("client.add_client", "client.add_client")
    permission_required = "client.add_client"
    permission_denied_message = _("You do not have permission to access this page.")
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
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    UpdateView,
):
    # permission_required = ["client.change_client", "client.change_client"]
    permission_required = "client.change_client"
    permission_denied_message = _("You do not have permission to access this page.")
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
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    DeleteView,
):
    template_name = "core/crudl/delete.html"
    # permission_required = ["client.delete_client", "client.delete_client"]
    permission_required = "client.delete_client"
    permission_denied_message = _("You do not have permission to access this page.")
    model = ClientProxy
    success_message = _("Client deleted successfully")
    success_url = reverse_lazy("dashboard:client:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Delete client"))
        context.setdefault("cancel_url", "dashboard:client:list")
        context.setdefault("object", self.get_object())
        context.setdefault("object_name", "client")
        context.setdefault("form_css_id", "clientDeleteForm")
        return context


class ClientDetailsView(
    PermissionRequiredMixin,
    UserPassesTestMixin,
    BWLoginRequiredMixin,
    BWCacheViewMixin,
    BWSectionDescriptionHelperMixin,
    DetailView,
):
    template_name = "client/details.html"

    model = ClientProxy
    # permission_required = ["client.view_client", "client.view_client"]
    permission_required = "client.view_client"
    permission_denied_message = _("You do not have permission to access this page.")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _(f"Client - {self.get_object().name}"))
        job_form = JobMiniForm(
            initial={"client": self.get_object().pk}, client=self.get_object()
        )
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
            removed_fields=["task", "status", "job"],
            hidden_inputs={"field_names": ["client"]},
        )
        note_form = NoteForm(
            renderer=BWFormRenderer(),
            initial={"client": self.get_object()},
            removed_fields=["task", "job"],
            hidden_inputs={"field_names": ["client"]},
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
        client_assign_bookkeeper_form = AssignBookkeeperForm(
            renderer=BWFormRenderer(), client=self.get_object()
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
        context.setdefault("client_assign_bookkeeper_form", client_assign_bookkeeper_form)
        return context

    def test_func(self) -> bool:
        user_type = self.request.user.user_type
        if user_type == CON_MANAGER or user_type == CON_ASSISTANT:
            return True
        else:
            bookkeeper = self.request.user.bookkeeper
            check = self.get_object().bookkeepers.filter(pk=bookkeeper.pk).exists()
            return check
