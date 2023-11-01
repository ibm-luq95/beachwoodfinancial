# -*- coding: utf-8 -*-#
from django.urls import path, include
from site_settings.views import (
    SiteSettingsFormView,
    ApplicationConfigurationsFormView,
    SectionDescriptionCreateView,
    SectionDescriptionListView,
    SectionDescriptionUpdateView,
)

app_name = "site_settings"

urlpatterns = [
    path("web-app", SiteSettingsFormView.as_view(), name="web_app_settings"),
    path(
        "app-configs",
        ApplicationConfigurationsFormView.as_view(),
        name="app_configs_settings",
    ),
    path(
        "section-description/",
        include(
            (
                [
                    path("create", SectionDescriptionCreateView.as_view(), name="create"),
                    path("", SectionDescriptionListView.as_view(), name="list"),
                    path(
                        "update/<uuid:pk>",
                        SectionDescriptionUpdateView.as_view(),
                        name="update",
                    ),
                ],
                "section_description",
            ),
            namespace="section_description",
        ),
    ),
]
