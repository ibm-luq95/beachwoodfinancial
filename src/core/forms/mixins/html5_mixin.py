# -*- coding: utf-8 -*-#
from django import forms


class Html5Mixin:
    """
    Mixin for form classes. Adds HTML5 features to forms for client
    side validation by the browser, like a "required" attribute and
    "email" and "url" input types.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if hasattr(self, "fields"):
            first_field = None

            for name, field in self.fields.items():
                # self.fields[name].widget.attrs.update({"class": "input"})
                # Autofocus first non-hidden field
                if not first_field and not field.widget.is_hidden:
                    first_field = field
                    first_field.widget.attrs["autofocus"] = ""
                # self.fields[name].widget.attrs.update({"class": "bkchlst-input"})
                if isinstance(field, forms.EmailField):
                    self.fields[name].widget.input_type = "email"
                elif isinstance(field, forms.URLField):
                    self.fields[name].widget.input_type = "url"
                    # self.fields[name].widget.attrs.update({"class": "input", "value": "https://"})
                elif isinstance(field, forms.DateField):
                    self.fields[name].widget.input_type = "date"
                    # self.fields[name].widget.attrs.update({"class": "input"})
                elif isinstance(field, forms.DateTimeField):
                    self.fields[name].widget.input_type = "datetime-local"
                    # self.fields[name].widget.attrs.update({"class": "input"})
                if field.required:
                    self.fields[name].widget.attrs["required"] = ""
