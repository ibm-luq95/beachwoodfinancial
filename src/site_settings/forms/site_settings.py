# -*- coding: utf-8 -*-#
from django import forms

from site_settings.models import SiteSettings
from core.forms import BaseModelFormMixin
from core.constants.form import EXCLUDED_FIELDS


class SiteSettingsForm(BaseModelFormMixin):
    def __init__(self, *args, **kwargs):
        super(SiteSettingsForm, self).__init__(*args, **kwargs)
        # self.fields["slug"].widget.attrs.update({"readonly": "readonly"})

    class Meta(BaseModelFormMixin.Meta):
        model = SiteSettings
        exclude = EXCLUDED_FIELDS
        # fieldsets = ("SEO", {"fields": ("title", "description", "keywords")})
