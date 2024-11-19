# -*- coding: utf-8 -*-#
from typing import Optional

from django import forms
from django.core.exceptions import ValidationError
from django.db import transaction
from django.utils.translation import gettext as _

from core.forms import BaseModelFormMixin, JoditFormMixin
from core.forms.mixins.base_form_mixin import BWBaseFormMixin
from core.forms.mixins.js_modal_form_renderer_mixin import BWJSModalFormRendererMixin
from core.forms.mixins.remove_fields_mixin import RemoveFieldsMixin
from core.forms.mixins.set_field_to_hidden import SetFieldsInputsHiddenMixin
from staff_briefcase.models import StaffNotes, StaffBriefcase


class BriefcaseNoteMiniForm(
    RemoveFieldsMixin, BWJSModalFormRendererMixin, BWBaseFormMixin
):
    def __init__(self, removed_fields: Optional[list] = None, *args, **kwargs):
        super(BWBaseFormMixin, self).__init__(*args, **kwargs)
        RemoveFieldsMixin.__init__(self, removed_fields=removed_fields)

    title = forms.CharField(label=_("Title"))
    note = forms.CharField(label=_("Note"), widget=forms.Textarea)
    briefcase = forms.UUIDField(widget=forms.HiddenInput)


class StaffNotesForm(BaseModelFormMixin, SetFieldsInputsHiddenMixin, JoditFormMixin):
    briefcase = forms.ModelChoiceField(
        queryset=StaffBriefcase.objects.all(), label=_("Briefcase"), required=False
    )

    def __init__(
        self,
        hidden_inputs: Optional[dict] = None,
        is_update_view: Optional[bool] = False,
        *args,
        **kwargs,
    ):
        super(StaffNotesForm, self).__init__(*args, **kwargs)
        SetFieldsInputsHiddenMixin.__init__(self, hidden_inputs=hidden_inputs)
        self.is_update_view = is_update_view
        if self.is_update_view is True:
            if self.instance.briefcase.exists() is True:
                self.fields["briefcase"].initial = self.instance.briefcase.get()

    class Meta(BaseModelFormMixin.Meta):
        model = StaffNotes

    def save(self, commit=True):
        try:
            note = super().save(commit=False)
            with transaction.atomic():

                if commit is True:
                    self.cleaned_data.get("briefcase").notes.remove(note)
                    self.cleaned_data.get("briefcase").save()
                    self.cleaned_data.get("briefcase").notes.add(note)
                    self.cleaned_data.get("briefcase").save()
                    note.save()
            return note
        except Exception as e:
            raise ValidationError(str(e))
