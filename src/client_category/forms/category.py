# -*- coding: utf-8 -*-#
from typing import Any
from django.utils.translation import gettext as _

from django.core.exceptions import ValidationError

from client_category.models import ClientCategory
from core.forms import BaseModelFormMixin


class ClientCategoryForm(BaseModelFormMixin):
    field_order = ["name", "status"]

    def __init__(self, *args, **kwargs):
        super(ClientCategoryForm, self).__init__(*args, **kwargs)

    def clean(self) -> dict[str, Any] | None:
        cleaned_data = super().clean()
        check = ClientCategory.original_objects.filter(name=cleaned_data.get("name"))
        if check.exists():
            # self.add_error("name", cleaned_data.get('name'))
            raise ValidationError(
                _(f"The name: {cleaned_data.get('name')} exists!"), code="invalid"
            )
        return cleaned_data

    class Meta(BaseModelFormMixin.Meta):
        model = ClientCategory
