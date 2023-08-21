# -*- coding: utf-8 -*-#
from typing import Optional

from core.forms import BaseModelFormMixin, JoditFormMixin
from core.forms.mixins.remove_fields_mixin import RemoveFieldsMixin
from core.forms.mixins.set_field_to_hidden import SetFieldsInputsHiddenMixin
from note.models import Note
from django import forms


class NoteForm(
    BaseModelFormMixin, RemoveFieldsMixin, SetFieldsInputsHiddenMixin, JoditFormMixin
):
    def __init__(
        self,
        client=None,
        note_section=None,
        add_jodit_css_class=False,
        removed_fields: Optional[list] = None,
        hidden_inputs: Optional[dict] = None,
        *args,
        **kwargs,
    ):
        super(NoteForm, self).__init__(*args, **kwargs)
        RemoveFieldsMixin.__init__(self, removed_fields=removed_fields)
        JoditFormMixin.__init__(self, add_jodit_css_class=add_jodit_css_class)
        SetFieldsInputsHiddenMixin.__init__(self, hidden_inputs=hidden_inputs)
        if client is not None:
            self.fields["client"].initial = client
            self.fields.pop("task")
            self.fields.pop("job")
        if note_section is not None:
            self.fields["note_section"].initial = note_section

        self.fields.pop("status")

    class Meta(BaseModelFormMixin.Meta):
        model = Note
        # fields = "__all__"
        widgets = {"body": forms.Textarea(attrs={"class": "rich-editor"})}
