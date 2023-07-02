from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import (
    UpdateView,
)

from core.cache import BWCacheViewMixin
from core.views.mixins import (
    BWLoginRequiredMixin,
    BWManagerAccessMixin,
)
from site_settings.forms import ApplicationConfigurationsForm
from site_settings.models import ApplicationConfigurations


class ApplicationConfigurationsFormView(
    BWLoginRequiredMixin,
    BWManagerAccessMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    UpdateView,
):
    # permission_required = "client.add_client"
    template_name = "site_settings/application_configuration.html"
    form_class = ApplicationConfigurationsForm
    success_message = _("Application configurations updated successfully")
    success_url = reverse_lazy("dashboard:site_settings:app_configs_settings")
    model = ApplicationConfigurations

    def get_object(self, queryset=None):
        obj = self.model.objects.select_related().filter(slug="app-configs").first()
        if not obj:
            messages.warning(self.request, _("No web app settings!"))
        return obj

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Update site settings"))
        return context
