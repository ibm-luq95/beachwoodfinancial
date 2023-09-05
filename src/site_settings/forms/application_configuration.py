# -*- encoding: utf-8 -*-
from site_settings.models import ApplicationConfigurations
from core.forms import BaseModelFormMixin
from core.constants.form import EXCLUDED_FIELDS


class ApplicationConfigurationsForm(BaseModelFormMixin):
    def __init__(self, *args, **kwargs):
        super(ApplicationConfigurationsForm, self).__init__(*args, **kwargs)
        # self.fields["slug"].widget.attrs.update({"readonly": "readonly"})

    class Meta(BaseModelFormMixin.Meta):
        model = ApplicationConfigurations
        exclude = EXCLUDED_FIELDS
