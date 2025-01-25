# -*- coding: utf-8 -*-#
from django.contrib import messages
from django.views.generic import TemplateView
from django.utils.translation import gettext as _

from core.views.mixins import BWLoginRequiredMixin


class DashboardView(BWLoginRequiredMixin, TemplateView):
    template_name = "dashboard/cfo/dashboard.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("CFO dashboard"))
        messages.set_level(self.request, messages.DEBUG)
        return context
