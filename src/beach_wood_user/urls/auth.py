# -*- coding: utf-8 -*-#
from django.contrib.auth.views import LogoutView
from django.urls import path

from beach_wood_user.views import BWLoginView, BWForgetPasswordView

app_name = "auth"

urlpatterns = [
    path("login", BWLoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("reset", BWForgetPasswordView.as_view(), name="reset"),
]
