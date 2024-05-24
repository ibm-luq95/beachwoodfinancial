# -*- coding: utf-8 -*-#
from django.forms.renderers import TemplatesSetting


class BWFormRenderer(TemplatesSetting):
    """
    Custom form renderer for the BW application.

    Extends Django's built-in TemplatesSetting class to provide a custom form template.

    Attributes:
    form_template_name : str
        The name of the HTML template file to be used for rendering forms.

    """

    form_template_name = "core/config/forms/modal_form_snippets.html"
