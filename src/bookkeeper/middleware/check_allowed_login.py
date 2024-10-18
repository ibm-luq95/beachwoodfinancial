# -*- coding: utf-8 -*-#
from django.contrib import messages
from django.contrib.auth import logout
from django.http import HttpRequest
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _

from core.cache import BWCacheHandler
from core.constants.site_settings import WEB_APP_SITE_SETTINGS_KEY
from core.utils import debugging_print


class CheckAllowedLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_view(
        self, request: HttpRequest, view_func, view_args: list, view_kwargs: dict
    ):
        if request.user.is_authenticated:
            # print(request.get_host())
            # check if the user type is bookkeeper or assistants
            if (
                request.user.user_type == "bookkeeper"
                or request.user.user_type == "assistants"
            ):
                site_settings = BWCacheHandler.get_item(
                    request.get_host(), WEB_APP_SITE_SETTINGS_KEY
                )
                # TODO: check if site_settings is None, for test cases
                # print(request.get_host())
                # print("###################")
                # print(site_settings)
                if site_settings is not None:
                    if (
                        site_settings.get("can_bookkeepers_login") is False
                        or site_settings.get("can_assistants_login") is False
                    ):
                        messages.error(
                            request,
                            _("You not allowed to login, please contact the administrator"),
                        )
                        logout(request)
                        return redirect(reverse_lazy("auth:login"))
