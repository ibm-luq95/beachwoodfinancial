from django.contrib import messages
from django.contrib.auth import logout
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import RedirectView
from django.utils.translation import gettext as _


class BWLogoutView(RedirectView):
    """
    Provides users the ability to logout
    """

    url: str | None = reverse_lazy("auth:login")

    def get(self, request, *args, **kwargs) -> HttpResponse:
        logout(request)
        messages.success(request, _("You are now logged out successfully."))
        return super(BWLogoutView, self).get(request, *args, **kwargs)
