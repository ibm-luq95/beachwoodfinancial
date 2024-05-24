# -*- coding: utf-8 -*-#
from django.urls import reverse_lazy


class UpdateReturnPreviousMixin:
    """
    Mixin class that adds functionality to update the previous URL and retrieve the success
    URL.

    This mixin class provides the following methods:

    - `get_context_data(self, **kwargs)`: Retrieves the context data for the view, including the previous URL.
    - `get_success_url(self) -> str`: Returns the URL to redirect to after processing a valid form.

    Attributes:
        BASE_SUCCESS_URL (str): The base success URL to use if the previous URL is not available.

    """

    def get_context_data(self, **kwargs):
        """
        Retrieves the context data for the view, including the previous URL.

        This method calls the base implementation to get the context and then adds the previous URL to the session.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            dict: The context data for the view, including the previous URL.

        """
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        prev_url = self.request.META.get("HTTP_REFERER")
        self.request.session["prev_url"] = prev_url
        self.request.session.modified = True
        return context

    def get_success_url(self) -> str:
        """
        Returns the URL to redirect to after processing a valid form.

        This method retrieves the previous URL from the session, deletes it from the session,
        and returns it as the success URL. If the previous URL is not available, it uses the base success URL.

        Returns:
            str: The URL to redirect to after processing a valid form.

        """
        prev_url = self.request.session.get("prev_url")
        del self.request.session["prev_url"]
        self.request.session.modified = True
        if prev_url is not None:
            return str(prev_url)  # success_url may be lazy
        else:
            return reverse_lazy(self.BASE_SUCCESS_URL)
