from typing import Any

from core.constants.form import EXCLUDED_FIELDS
from crispy_forms.helper import FormHelper
from django import forms
from django.forms import ValidationError
from django.utils.translation import gettext as _

from .html5_mixin import Html5Mixin


class BaseModelFormMixin(Html5Mixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseModelFormMixin, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    class Meta:
        exclude = EXCLUDED_FIELDS

    def clean(self) -> dict[str, Any] | None:
        cleaned_data = super().clean()
        for name, field in self.fields.items():
            if isinstance(field, forms.URLField):
                if (
                        cleaned_data.get(name) == "https://"
                        or cleaned_data.get(name) == "http://"
                ):
                    raise ValidationError({name: _("Please enter valid url")})
        return cleaned_data
