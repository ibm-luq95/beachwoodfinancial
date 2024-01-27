from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import (
    UpdateView,
)

from core.cache import BWCacheViewMixin
from core.constants.site_settings import SITE_SETTINGS_DB_SLUG
from core.views.mixins import (
    BWLoginRequiredMixin,
)
from site_settings.forms import SiteSettingsForm
from site_settings.models import SiteSettings


class SiteSettingsFormView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWCacheViewMixin,
    SuccessMessageMixin,
    UpdateView,
):
    permission_required = "manager.manager_user"
    permission_denied_message = _("You do not have permission to access this page.")
    template_name = "site_settings/site_settings.html"
    form_class = SiteSettingsForm
    success_message = _("Site settings updated successfully")
    success_url = reverse_lazy("dashboard:site_settings:web_app_settings")
    model = SiteSettings

    def get_object(self, queryset=None):
        obj = self.model.objects.filter(slug=SITE_SETTINGS_DB_SLUG).first()
        if not obj:
            messages.warning(self.request, _("No web app site settings!"))
        return obj

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Update site settings"))
        return context

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        return super().form_valid(form)
