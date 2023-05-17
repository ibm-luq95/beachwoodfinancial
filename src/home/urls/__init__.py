# -*- coding: utf-8 -*-#
from django.urls import path

from home.views import LandingPageView, AboutView, FAQView, PricesView, ContactView

app_name = "home"

urlpatterns = [
    path("", LandingPageView.as_view(), name="landing"),
    path("about", AboutView.as_view(), name="about"),
    path("faq", FAQView.as_view(), name="faq"),
    path("prices", PricesView.as_view(), name="prices"),
    path("contact", ContactView.as_view(), name="contact"),
]
