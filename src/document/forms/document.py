# -*- coding: utf-8 -*-#
from typing import Optional

from core.constants.form import EXCLUDED_FIELDS
from core.forms import BaseModelFormMixin
from core.forms.mixins.remove_fields_mixin import RemoveFieldsMixin
from core.forms.mixins.set_field_to_hidden import SetFieldsInputsHiddenMixin
from document.models import Document


class DocumentForm(BaseModelFormMixin, RemoveFieldsMixin, SetFieldsInputsHiddenMixin):
    # auto_id = "doct_"
    # default_renderer = Rend()

    def __init__(
        self,
        removed_fields: Optional[list] = None,
        hidden_inputs: Optional[dict] = None,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        RemoveFieldsMixin.__init__(self, removed_fields=removed_fields)
        SetFieldsInputsHiddenMixin.__init__(self, hidden_inputs=hidden_inputs)
        # if document_section is not None:
        #     self.fields["document_section"].initial = document_section
        #     # self.fields["document_section"].widget.attrs.update({"class": "readonly-select cursor-not-allowed"})
        #     # self.fields.pop("task")
        #     self.fields.pop("job")
        if self.initial.get("client") is not None:
            pass

        # if client is not None:
        #     self.fields["client"].initial = client
        #
        # if is_update is True:
        #     self.fields["document_file"].required = False
        #     self.fields["document_file"].widget.attrs["readonly"] = True

    class Meta(BaseModelFormMixin.Meta):
        model = Document
        exclude = EXCLUDED_FIELDS
