# -*- coding: utf-8 -*-#
from typing import Optional

from core.constants import EXCLUDED_FIELDS
from core.forms import BaseModelFormMixin, JoditFormMixin
from core.forms.mixins.remove_fields_mixin import RemoveFieldsMixin
from core.forms.widgets import RichHTMLEditorWidget
from discussion.models import DiscussionProxy


class DiscussionForm(BaseModelFormMixin, RemoveFieldsMixin, JoditFormMixin):
    def __init__(
        self,
        add_jodit_css_class=False,
        removed_fields: Optional[list] = None,
        *args,
        **kwargs,
    ):
        super(DiscussionForm, self).__init__(*args, **kwargs)
        RemoveFieldsMixin.__init__(self, removed_fields=removed_fields)
        JoditFormMixin.__init__(self, add_jodit_css_class=add_jodit_css_class)
        # self.fields["body"].widget.attrs.update({"rows": 5, "cols": 10})

    class Meta(BaseModelFormMixin.Meta):
        model = DiscussionProxy
        exclude = EXCLUDED_FIELDS + ["is_seen"]
        widgets = {"body": RichHTMLEditorWidget}
