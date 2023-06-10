# -*- coding: utf-8 -*-#
from typing import Any, Optional, Sequence, Tuple
from django import forms

from core.choices import BeachWoodUserTypeEnum

from django.forms.renderers import TemplatesSetting

from core.forms.widgets import BWPasswordInputWidget
from core.utils import debugging_print


class FormRenderer(TemplatesSetting):
    form_template_name = "beach_wood_user/widgets/form_snippet.html"


class BWUserTypeRadioSelect(forms.RadioSelect):
    template_name = "beach_wood_user/widgets/user_types.html"
    option_template_name = "beach_wood_user/widgets/radio_option.html"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs.update({"class": "relative ddddd"})
        # self.checked_attribute = ""
        debugging_print(self.checked_attribute)
        # debugging_print(dir(self))


class BWEmailInput(forms.EmailInput):
    # template_name = "beach_wood_user/widgets/email.html"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize the widget here
        self.attrs["class"] = (
            f"block w-full px-4 py-3 text-sm border-gray-200 rounded-md focus:border-blue-500 "
            f"focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400"
        )


class BWLoginForm(forms.Form):
    default_renderer = FormRenderer()
    user_type = forms.ChoiceField(
        label=False,
        choices=BeachWoodUserTypeEnum.choices,
        required=True,
        widget=BWUserTypeRadioSelect,
    )
    email = forms.EmailField(
        label="Email Address",
        required=True,
        widget=BWEmailInput,
        help_text="DESS",
        error_messages={"required": "This is required"},
    )
    password = forms.CharField(widget=BWPasswordInputWidget, required=True)
