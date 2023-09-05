# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django.views.generic import DetailView

from assistant.forms import AssistantForm
from beach_wood_user.forms import BWPermissionsForm
from beach_wood_user.models import BWUser
from bookkeeper.forms import BookkeeperForm
from client.models import ClientProxy
from core.config.forms import BWFormRenderer
from core.views.mixins import BWLoginRequiredMixin
from manager.forms import ManagerForm
from special_assignment.forms import MiniSpecialAssignmentForm


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
        clients = ClientProxy.objects.all()
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
        context.setdefault("clients", clients)
        context.setdefault("special_assignment_form", special_assignment_form)
        context.setdefault("staff_form", staff_form)
        context.setdefault("permissions_form", permissions_form)
        return context
