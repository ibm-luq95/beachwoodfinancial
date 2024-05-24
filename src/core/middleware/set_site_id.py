# -*- coding: utf-8 -*-#
from typing import Any, List, Dict

from django.conf import settings
from django.contrib.sites.models import Site
from django.http import HttpRequest


class MultiHostMiddleware:
    """
    Middleware class to handle multiple host configurations.

    This middleware class is responsible for processing each request before the view is called. It then processes the response after the view is executed.

    Methods:
        __init__: Initializes the middleware with the get_response function.
        __call__: Executes code before and after the view is called.
        process_view: Handles processing the view based on the request parameters.

    Attributes:
        get_response: The function responsible for getting the response.

    """

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
        self,
        request: HttpRequest,
        view_func: Any,
        view_args: List[Any],
        view_kwargs: Dict[str, Any],
    ) -> None:
        """
        Process the view by setting the SITE_ID based on the request's host.

        Args:
            request (HttpRequest): The incoming request.
            view_func (Any): The view function.
            view_args (List[Any]): The arguments for the view function.
            view_kwargs (Dict[str, Any]): The keyword arguments for the view function.

        Returns:
            None

        """
        try:
            # TODO: Check if settings.SITE_ID already has value
            s = Site.objects.filter(domain=request.get_host())
            if s:
                s = s.first()
                settings.SITE_ID = s.id
        except KeyError:
            pass
