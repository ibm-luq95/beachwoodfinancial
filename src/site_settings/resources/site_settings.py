# -*- coding: utf-8 -*-#
from import_export import resources

from site_settings.models import SiteSettings


class SiteSettingsResource(resources.ModelResource):
    class Meta:
        model = SiteSettings
