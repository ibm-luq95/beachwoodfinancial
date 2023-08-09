# -*- coding: utf-8 -*-#
from core.constants import EXCLUDED_FIELDS
from core.forms import BaseModelFormMixin, JoditFormMixin
from discussion.models import DiscussionProxy


class DiscussionForm(BaseModelFormMixin, JoditFormMixin):
    def __init__(self, add_jodit_css_class=False, *args, **kwargs):
        super(DiscussionForm, self).__init__(*args, **kwargs)
        JoditFormMixin.__init__(self, add_jodit_css_class=add_jodit_css_class)
        self.fields["body"].widget.attrs.update({"rows": 5, "cols": 10})

    class Meta(BaseModelFormMixin.Meta):
        model = DiscussionProxy
        exclude = EXCLUDED_FIELDS + ["is_seen"]
