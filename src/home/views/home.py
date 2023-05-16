# -*- coding: utf-8 -*-#
from django.views.generic import TemplateView

from core.utils import get_trans_txt


class LandingPageView(TemplateView):
    template_name = "home/landing_page.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Home"))
        return context


class AboutView(TemplateView):
    template_name = "home/about.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("About US"))
        return context
