# -*- coding: utf-8 -*-#

from django import forms


class JoditFormMixin:
    def __init__(self, add_jodit_css_class=False):
        if add_jodit_css_class is True:
            for field_name in self.fields:
                if isinstance(self.fields.get(field_name).widget, forms.Textarea):
                    self.fields[field_name].widget.attrs.update(
                        {"class": "wyswyg-textarea"}
                    )
