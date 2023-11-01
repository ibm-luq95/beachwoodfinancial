# -*- coding: utf-8 -*-#
from django import forms
from django.db import transaction, DatabaseError, IntegrityError
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

from core.forms.widgets import RichHTMLEditorWidget
from site_settings.models import SectionDescription
from core.forms import BaseModelFormMixin
from core.constants.form import EXCLUDED_FIELDS


class SectionDescriptionForm(BaseModelFormMixin):
    def __init__(self, *args, **kwargs):
        super(SectionDescriptionForm, self).__init__(*args, **kwargs)
        # self.fields["slug"].widget.attrs.update({"readonly": "readonly"})

    class Meta(BaseModelFormMixin.Meta):
        model = SectionDescription
        exclude = EXCLUDED_FIELDS
        widgets = {"description": RichHTMLEditorWidget(required=False)}
        # fieldsets = ("SEO", {"fields": ("title", "description", "keywords")})

    def save(self, commit=True):
        # Save the provided password in hashed format
        try:
            section_description_obj = super().save(commit=False)
            with transaction.atomic():
                if commit:
                    section_description_obj.save()
                return section_description_obj
        except IntegrityError as ex:
            # raise self.ValidationError("DDDD")
            self.add_error("section_title", _("Section title duplicate with another section"))
            raise ValidationError(str(ex), code="invalid")
