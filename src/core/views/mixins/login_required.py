# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class BWLoginRequiredMixin(LoginRequiredMixin):
    """
    Mixin class that requires the user to be authenticated before accessing the view.

    Attributes:
        login_url (str): The URL to redirect to for login.

    """

    login_url = reverse_lazy("auth:login")
