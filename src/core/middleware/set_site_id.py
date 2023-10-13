# -*- coding: utf-8 -*-#
from django.conf import settings
from django.contrib.sites.models import Site
from django.http import HttpRequest


class MultiHostMiddleware:
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
        try:
            s = Site.objects.get(domain=request.get_host())
            if s:
                settings.SITE_ID = s.id
        except KeyError:
            pass  # use default urlconf (settings.ROOT_URLCONF)
