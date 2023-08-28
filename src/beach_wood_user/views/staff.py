# -*- coding: utf-8 -*-#

from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django.views.generic import DetailView

from beach_wood_user.models import BWUser
from client.models import ClientProxy
from core.choices import JobStatusEnum, JobStateEnum
from core.config.forms import BWFormRenderer
from core.utils.developments.utils import get_list_from_text_choices
from core.views.mixins import BWManagerAccessMixin, BWLoginRequiredMixin
from special_assignment.forms import MiniSpecialAssignmentForm


class StaffMemberDetailsView(
    BWLoginRequiredMixin, BWManagerAccessMixin, SuccessMessageMixin, DetailView
):
    template_name = "beach_wood_user/details.html"
    model = BWUser

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", f"{self.object.fullname} - " + self.object.user_type.title())
        stats_list = get_list_from_text_choices(JobStateEnum)
        status_list = get_list_from_text_choices(JobStatusEnum)
        clients = ClientProxy.objects.all()
        special_assignment_form = MiniSpecialAssignmentForm(
            renderer=BWFormRenderer(),
            initial={"assigned_by": self.request.user.pk, "client": self.get_object().pk},
        )
        context.setdefault("stats_list", stats_list)
        context.setdefault("status_list", status_list)
        context.setdefault("clients", clients)
        context.setdefault("special_assignment_form", special_assignment_form)
        return context
