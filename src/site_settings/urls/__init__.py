# -*- coding: utf-8 -*-#
from django.urls import path
from site_settings.views import SiteSettingsFormView, ApplicationConfigurationsFormView

app_name = "site_settings"

urlpatterns = [
    path(
        "web-app",
        SiteSettingsFormView.as_view(),
        name="web_app_settings",
    ),
    path(
        "app-configs",
        ApplicationConfigurationsFormView.as_view(),
        name="app_configs_settings",
    ),
]
