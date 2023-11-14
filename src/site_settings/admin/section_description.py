# -*- coding: utf-8 -*-#
from django.contrib import admin

from site_settings.models import SectionDescription
from core.admin import BWBaseAdminModelMixin


@admin.register(SectionDescription)
class SectionDescriptionAdmin(BWBaseAdminModelMixin):
    list_display = ("section_title", "slug", "site")
