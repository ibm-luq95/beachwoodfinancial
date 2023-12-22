# -*- coding: utf-8 -*-#
from django.urls import reverse_lazy


class UpdateReturnPreviousMixin:
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        prev_url = self.request.META.get("HTTP_REFERER")
        self.request.session["prev_url"] = prev_url
        self.request.session.modified = True
        return context

    def get_success_url(self) -> str:
        """Return the URL to redirect to after processing a valid form."""
        prev_url = self.request.session.get("prev_url")
        del self.request.session["prev_url"]
        self.request.session.modified = True
        if prev_url is not None:
            return str(prev_url)  # success_url may be lazy
        else:
            return reverse_lazy(self.BASE_SUCCESS_URL)
