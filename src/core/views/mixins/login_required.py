# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class BaseLoginRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy("users:auth:login")
