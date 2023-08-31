# -*- coding: utf-8 -*-#

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db import transaction
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import DeleteView, DetailView, ListView, FormView
from django.views.generic.detail import SingleObjectMixin

from assistant.filters import AssistantFilter
from assistant.forms import AssistantForm
from assistant.models import AssistantProxy
from beach_wood_user.models import BWUser
from core.cache import BWCacheViewMixin
from core.choices import JobStatusEnum, JobStateEnum
from core.constants import LIST_VIEW_PAGINATE_BY
from core.utils.developments.utils import get_list_from_text_choices
from core.views.mixins import BWBaseListViewMixin, BWLoginRequiredMixin


class AssistantListView(
    BWLoginRequiredMixin,
    PermissionRequiredMixin,
    BWCacheViewMixin,
    BWBaseListViewMixin,
    ListView,
):
    permission_required = ["assistant.can_view_list"]
    permission_denied_message = _("You do not have permission to access this page.")
    template_name = "assistant/list.html"
    model = AssistantProxy
    paginate_by = LIST_VIEW_PAGINATE_BY
    list_type = "list"
    queryset = AssistantProxy.objects.get_queryset().order_by("-user__created_at")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = _("Assistants")
        context.setdefault("filter_form", self.filterset.form)
        context.setdefault("list_type", self.list_type)
        context.setdefault("page_header", "notes".title())

        # debugging_print(self.filterset.form["name"])
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = AssistantFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs


class AssistantCreateView(
    SuccessMessageMixin,
    BWLoginRequiredMixin,
    PermissionRequiredMixin,
    BWCacheViewMixin,
    FormView,
):
    permission_required = ["assistant.add_assistant", "assistant.add_assistantproxy"]
    permission_denied_message = _("You do not have permission to access this page.")
    template_name = "assistant/create.html"
    form_class = AssistantForm
    success_message = _("Assistant created successfully")
    success_url = reverse_lazy("dashboard:management_assistant:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Create a new assistant"))
        return context

    def form_valid(self, form: AssistantForm):
        """If the form is valid, save the associated model."""
        try:
            with transaction.atomic():
                user_details = {
                    "first_name": form.cleaned_data.get("first_name"),
                    "last_name": form.cleaned_data.get("last_name"),
                    "email": form.cleaned_data.get("email"),
                    "user_type": form.STAFF_MEMBER_TYPE,
                }
                profile_details = {
                    "linkedin": form.cleaned_data.get("linkedin"),
                    "instagram": form.cleaned_data.get("instagram"),
                    "github": form.cleaned_data.get("github"),
                    "facebook": form.cleaned_data.get("facebook"),
                    "twitter": form.cleaned_data.get("twitter"),
                    "address": form.cleaned_data.get("address"),
                    "phone_number": form.cleaned_data.get("phone_number"),
                    "bio": form.cleaned_data.get("bio"),
                    "profile_picture": form.cleaned_data.get("profile_picture"),
                }
                new_user = BWUser.objects.create(**user_details)
                new_user.set_password(form.cleaned_data.get("password"))
                new_user.assistant.assistant_type = form.cleaned_data.get("assistant_type")
                new_user.assistant.save()
                for attr, value in profile_details.items():
                    setattr(new_user.assistant.profile, attr, value)
                new_user.assistant.profile.save()
            return super().form_valid(form)
        except Exception as ex:
            raise Exception(str(ex))


class AssistantDetailsView(
    BWLoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DetailView
):
    template_name = "assistant/details.html"
    model = AssistantProxy
    permission_required = ["assistant.change_assistant", "assistant.change_assistantproxy"]
    permission_denied_message = _("You do not have permission to access this page.")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", f"{self.object.user.fullname} " + _("Assistant"))
        stats_list = get_list_from_text_choices(JobStateEnum)
        status_list = get_list_from_text_choices(JobStatusEnum)
        context.setdefault("stats_list", stats_list)
        context.setdefault("status_list", status_list)
        return context


class AssistantUpdateView(
    SuccessMessageMixin,
    BWLoginRequiredMixin,
    PermissionRequiredMixin,
    BWCacheViewMixin,
    SingleObjectMixin,
    FormView,
):
    permission_required = ["assistant.change_assistant", "assistant.change_assistantproxy"]
    permission_denied_message = _("You do not have permission to access this page.")
    template_name = "assistant/update.html"
    form_class = AssistantForm
    # success_message = _("Bookkeeper updated successfully")
    # success_url = reverse_lazy("dashboard:management_assistant:list")
    model = AssistantProxy

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        self.object = self.get_object()  # this must be before super()
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Update assistant"))
        return context

    def get_success_message(self, cleaned_data: dict[str, str]) -> str:
        return _(f"Assistant {self.object.user.fullname} updated successfully!")

    def get_object(self, queryset=None):
        """
        Retrieve the object that this view is displaying.
        """
        if queryset is None:
            queryset = self.get_queryset()
        # Retrieve the object

        return queryset.get(pk=self.kwargs["pk"])

    def get_success_url(self) -> str:
        """Return the URL to redirect to after processing a valid form."""
        success_url = reverse_lazy(
            "dashboard:management_assistant:update", kwargs={"pk": self.object.pk}
        )
        return str(success_url)  # success_url may be lazy

    def get_initial(self) -> dict:
        initial = super().get_initial()
        initial["email"] = self.object.user.email
        initial["first_name"] = self.object.user.first_name
        initial["last_name"] = self.object.user.last_name
        initial["bio"] = self.object.profile.bio
        initial["profile_picture"] = self.object.profile.profile_picture
        initial["assistant_type"] = self.object.assistant_type
        initial["address"] = self.object.profile.address
        initial["phone_number"] = self.object.profile.phone_number
        initial["facebook"] = self.object.profile.facebook
        initial["twitter"] = self.object.profile.twitter
        initial["github"] = self.object.profile.github
        initial["linkedin"] = self.object.profile.linkedin
        initial["instagram"] = self.object.profile.instagram

        return initial

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form: AssistantForm):
        """If the form is valid, save the associated model."""
        try:
            with transaction.atomic():
                assistant = self.object
                user_details = {
                    "first_name": form.cleaned_data.get("first_name"),
                    "last_name": form.cleaned_data.get("last_name"),
                    "email": form.cleaned_data.get("email"),
                    "user_type": form.STAFF_MEMBER_TYPE,
                }
                for key, value in user_details.items():
                    setattr(assistant.user, key, value)
                assistant.user.save()
                assistant.assistant_type = form.cleaned_data.get("assistant_type")
                assistant.save()
                profile_details = {
                    "linkedin": form.cleaned_data.get("linkedin"),
                    "instagram": form.cleaned_data.get("instagram"),
                    "github": form.cleaned_data.get("github"),
                    "facebook": form.cleaned_data.get("facebook"),
                    "twitter": form.cleaned_data.get("twitter"),
                    "address": form.cleaned_data.get("address"),
                    "phone_number": form.cleaned_data.get("phone_number"),
                    "bio": form.cleaned_data.get("bio"),
                    "profile_picture": form.cleaned_data.get("profile_picture"),
                }
                for attr, value in profile_details.items():
                    setattr(assistant.profile, attr, value)
                assistant.profile.save()
            return super().form_valid(form)
        except Exception as ex:
            raise Exception(str(ex))


class AssistantDeleteView(
    BWLoginRequiredMixin,
    PermissionRequiredMixin,
    BWCacheViewMixin,
    BWBaseListViewMixin,
    SuccessMessageMixin,
    DeleteView,
):
    permission_required = ["assistant.delete_assistant", "assistant.delete_assistantproxy"]
    permission_denied_message = _("You do not have permission to access this page.")
    template_name = "assistant/delete.html"
    model = AssistantProxy
    success_message = _("Assistant deleted successfully")
    success_url = reverse_lazy("dashboard:management_assistant:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Delete assistant"))
        return context
