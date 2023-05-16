# -*- coding: utf-8 -*-#
from django.urls import path, include

from home.views import LandingPageView, AboutView

app_name = "home"

urlpatterns = [
    path("", LandingPageView.as_view(), name="landing-page"),
    path("about", AboutView.as_view(), name="about-page"),
]
