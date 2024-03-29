# -*- coding: utf-8 -*-#
from django.contrib import messages
from django.views.generic import TemplateView
from django.utils.translation import gettext as _


class DashboardView(TemplateView):
    template_name = "dashboard/bookkeeper/dashboard.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Bookkeeper dashboard"))
        messages.set_level(self.request, messages.DEBUG)
        return context