# -*- coding: utf-8 -*-#
from django.contrib import messages
from django.views.generic import TemplateView
from django.utils.translation import gettext as _

from core.cache import BWCacheViewMixin
from core.views.mixins import BWLoginRequiredMixin, BWManagerAccessMixin


class DashboardViewBW(BWLoginRequiredMixin, BWManagerAccessMixin, BWCacheViewMixin, TemplateView):
    template_name = "dashboard/manager/dashboard.html"
    http_method_names = ["get"]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Manager dashboard"))
        messages.set_level(self.request, messages.DEBUG)
        return context
