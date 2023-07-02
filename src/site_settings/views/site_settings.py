from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import (
    UpdateView,
)

from core.cache import BWCacheViewMixin
from core.utils import debugging_print
from core.views.mixins import (
    BWLoginRequiredMixin,
    BWManagerAccessMixin,
)
from site_settings.forms import SiteSettingsForm
from site_settings.models import SiteSettings


class SiteSettingsFormView(
    BWLoginRequiredMixin,
    BWManagerAccessMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    UpdateView,
):
    # permission_required = "client.add_client"
    template_name = "site_settings/site_settings.html"
    form_class = SiteSettingsForm
    success_message = _("Site settings updated successfully")
    success_url = reverse_lazy("dashboard:site_settings:web_app_settings")
    model = SiteSettings

    def get_object(self, queryset=None):
        obj = self.model.objects.select_related().filter(slug="web-app").first()
        if not obj:
            messages.warning(self.request, _("No web app settings!"))
        return obj

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Update site settings"))
        return context

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        debugging_print(form.cleaned_data)
        return super().form_valid(form)
