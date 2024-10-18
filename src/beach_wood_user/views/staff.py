# -*- coding: utf-8 -*-#
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import DetailView
from django.views.generic import FormView
from django.views.generic.detail import SingleObjectMixin

from assistant.forms import AssistantForm
from beach_wood_user.forms import BWPermissionsForm, ProfileForm, ForceChangePasswordForm
from beach_wood_user.models import BWUser
from bookkeeper.forms import BookkeeperForm
from client.models import ClientProxy
from core.config.forms import BWFormRenderer
from core.views.mixins import BWLoginRequiredMixin
from manager.forms import ManagerForm
from special_assignment.forms import MiniSpecialAssignmentForm
from staff_briefcase.forms import (
    BriefcaseNoteMiniForm,
    BriefcaseDocumentMiniForm,
    BriefcaseAccountMiniForm,
)


class StaffMemberDetailsView(
    PermissionRequiredMixin, BWLoginRequiredMixin, SuccessMessageMixin, DetailView
):
    template_name = "beach_wood_user/details.html"
    model = BWUser
    http_method_names = ["get"]
    permission_required = [
        "beach_wood_user.view_bwuser",
        "beach_wood_user.view_profile",
        "beach_wood_user.developer_user",
        "assistant.assistant_has_full_manager_permissions",
    ]
    permission_denied_message = _("You do not have permission to access this page.")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault(
            "title", f"{self.object.fullname} - " + self.object.user_type.title()
        )
        clients = ClientProxy.objects.order_by("name")
        permissions_form = BWPermissionsForm(
            staff_user=self.get_object(), initial={"user": self.get_object().pk}
        )
        special_assignment_form = MiniSpecialAssignmentForm(
            renderer=BWFormRenderer(),
            initial={"assigned_by": self.request.user.pk, "client": self.get_object().pk},
        )
        # staff form
        staff_form = None
        staff_form_initial = self.get_object().get_staff_details()
        removed_fields = ["password", "profile_picture", "confirm_password"]
        # debugging_print(self.get_object().get_staff_details())
        if self.get_object().user_type == "bookkeeper":
            staff_form = BookkeeperForm(
                initial=staff_form_initial, removed_fields=removed_fields
            )
        elif self.get_object().user_type == "assistant":
            staff_form = AssistantForm(
                initial=staff_form_initial, removed_fields=removed_fields
            )
        elif self.get_object().user_type == "manager":
            staff_form = ManagerForm(
                initial=staff_form_initial, removed_fields=removed_fields
            )
        briefcase_note_form = BriefcaseNoteMiniForm(
            initial={"briefcase": self.get_object().briefcase.pk}
        )
        briefcase_document_form = BriefcaseDocumentMiniForm(
            initial={"briefcase": self.get_object().briefcase.pk}
        )
        briefcase_account_form = BriefcaseAccountMiniForm(
            initial={"briefcase": self.get_object().briefcase.pk}
        )

        context.setdefault("clients", clients)
        context.setdefault("special_assignment_form", special_assignment_form)
        context.setdefault("staff_form", staff_form)
        context.setdefault("permissions_form", permissions_form)
        context.setdefault("briefcase_note_form", briefcase_note_form)
        context.setdefault("briefcase_document_form", briefcase_document_form)
        context.setdefault("briefcase_account_form", briefcase_account_form)
        return context


class StaffProfileView(BWLoginRequiredMixin, SuccessMessageMixin, FormView, DetailView):
    template_name = "beach_wood_user/profile.html"
    model = BWUser
    http_method_names = ["get", "post"]
    # permission_required = "beach_wood_user.view_profile"
    permission_denied_message = _("You do not have permission to access this page.")
    form_class = ProfileForm
    success_message = _("Profile updated successfully!")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", f"{self.object.fullname}")
        return context

    def get_success_url(self) -> str:
        """Return the URL to redirect to after processing a valid form."""
        success_url = reverse_lazy(
            "dashboard:staff:staff-profile", kwargs={"pk": self.object.pk}
        )
        return str(success_url)  # success_url may be lazy

    def get_form_kwargs(self):
        # kwargs = super().get_form_kwargs()
        kwargs = {
            "initial": self.get_initial(),
            "prefix": self.get_prefix(),
        }
        kwargs.update(
            {
                "instance": self.get_object()
                .get_staff_member_object.get("staff_object")
                .profile
            }
        )
        if self.request.method in ("POST", "PUT"):
            kwargs.update(
                {
                    "data": self.request.POST,
                    "files": self.request.FILES,
                }
            )
        return kwargs

    def form_valid(self, form: ProfileForm):
        """If the form is valid, save the associated model."""
        form.save()
        self.object = self.get_object()
        return super().form_valid(form)

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        self.object = self.get_object()
        return self.render_to_response(self.get_context_data(form=form))


class StaffUpdatePasswordView(
    BWLoginRequiredMixin, SuccessMessageMixin, SingleObjectMixin, FormView
):
    form_class = ForceChangePasswordForm
    template_name = "beach_wood_user/update_password.html"
    model = BWUser
    http_method_names = ["get", "post"]
    context_object_name = "object"
    success_message = _("Password updated successfully!")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.setdefault(
            "title", _(f"Force update password - {self.get_object().fullname}")
        )
        # Add any additional context data if needed
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return self.render_to_response(self.get_context_data())

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        self.object = self.get_object()
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form: ForceChangePasswordForm):
        """If the form is valid, save the associated model."""
        # form.save()
        self.object = self.get_object()
        self.object.set_password(form.cleaned_data["password1"])
        self.object.save(update_fields=["password"])
        self.object = self.get_object()
        update_session_auth_hash(self.request, self.get_object())
        return super().form_valid(form)

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

    def get_success_url(self) -> str:
        """Return the URL to redirect to after processing a valid form."""
        success_url = reverse_lazy(
            "dashboard:staff:staff-update-password", kwargs={"pk": self.get_object().pk}
        )
        return str(success_url)  # success_url may be lazy
