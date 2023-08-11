# -*- coding: utf-8 -*-#
from django.forms.renderers import TemplatesSetting


class BWFormRenderer(TemplatesSetting):
    form_template_name = "core/config/forms/modal_form_snippets.html"
