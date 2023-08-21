# -*- coding: utf-8 -*-#
from typing import Optional
from django import forms

from client_category.models import ClientCategory
from django.utils.translation import gettext as _

from core.constants.file_types_validation import IMAGES_FT
from core.forms.mixins.base_form_mixin import BWBaseFormMixin
from core.forms.mixins.js_modal_form_renderer_mixin import BWJSModalFormRendererMixin
from core.forms.mixins.remove_fields_mixin import RemoveFieldsMixin
from core.utils import FileValidator
from important_contact.models import ImportantContact

file_validator = FileValidator(max_size=1024 * 1000, content_types=IMAGES_FT)


class ClientMiniForm(RemoveFieldsMixin, BWBaseFormMixin):
    def __init__(self, removed_fields: Optional[list] = None, *args, **kwargs):
        super(BWBaseFormMixin, self).__init__(*args, **kwargs)
        RemoveFieldsMixin.__init__(self, removed_fields=removed_fields)

    categories = forms.ModelChoiceField(
        queryset=ClientCategory.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    important_contacts = forms.ModelChoiceField(
        queryset=ImportantContact.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    logo = forms.ImageField(
        label=_("Client logo"), required=False, validators=[file_validator]
    )
