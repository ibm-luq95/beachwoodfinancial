# -*- coding: utf-8 -*-#
from typing import Optional

from django import forms


class RichHTMLEditorWidget(forms.widgets.Textarea):
    def __init__(self, attrs: Optional[dict] = None, *args, **kwargs):
        attrs = attrs or {}
        attrs.update({"class": "wyswyg-textarea"})
        super(RichHTMLEditorWidget, self).__init__(attrs)
