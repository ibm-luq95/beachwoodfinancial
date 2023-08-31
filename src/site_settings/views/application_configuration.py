from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import UpdateView

from core.cache import BWCacheViewMixin
from core.constants.site_settings import APP_CONFIGS_DB_SLUG
from core.views.mixins import BWLoginRequiredMixin
from site_settings.forms import ApplicationConfigurationsForm
from site_settings.models import ApplicationConfigurations


class ApplicationConfigurationsFormView(
    BWLoginRequiredMixin,
    PermissionRequiredMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    UpdateView,
):
    permission_required = "manager.manager_user"
    permission_denied_message = _("You do not have permission to access this page.")
    template_name = "site_settings/application_configuration.html"
    form_class = ApplicationConfigurationsForm
    success_message = _("Application configurations updated successfully")
    success_url = reverse_lazy("dashboard:site_settings:app_configs_settings")
    model = ApplicationConfigurations

    def get_object(self, queryset=None):
        obj = self.model.objects.filter(slug=APP_CONFIGS_DB_SLUG).first()
        if not obj:
            messages.warning(self.request, _("No web app configs!"))
        return obj

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Update web application configurations"))
        return context
