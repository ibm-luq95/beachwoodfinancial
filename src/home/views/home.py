# -*- coding: utf-8 -*-#
from django.contrib import messages
from django.views.generic import TemplateView

from core.utils import get_trans_txt


class LandingPageView(TemplateView):
    template_name = "home/landing_page.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Home"))
        messages.set_level(self.request, messages.DEBUG)
        return context


class AboutView(TemplateView):
    template_name = "home/about.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("About US"))
        return context


class FAQView(TemplateView):
    template_name = "home/faq.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("FAQs"))
        messages.set_level(self.request, messages.DEBUG)
        return context


class PricesView(TemplateView):
    template_name = "home/prices.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Prices"))
        messages.set_level(self.request, messages.DEBUG)
        return context


class ContactView(TemplateView):
    template_name = "home/contact.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Contact us"))
        messages.set_level(self.request, messages.DEBUG)
        return context
