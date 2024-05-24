# -*- coding: utf-8 -*-#

from django import forms


class JoditFormMixin:
    """
    A mixin class that adds the Jodit CSS class to the widgets of textarea fields.
    """

    def __init__(self, add_jodit_css_class: bool = False) -> None:
        """
        Initializes the JoditFormMixin instance.

        Args:
            add_jodit_css_class: A boolean flag indicating whether to add the Jodit CSS class to the widgets of textarea fields. Defaults to False.

        """
        if add_jodit_css_class is True:
            for field_name in self.fields:
                field = self.fields.get(field_name)
                if isinstance(field.widget, forms.Textarea):
                    field.widget.attrs.update({"class": "rich-editor"})
