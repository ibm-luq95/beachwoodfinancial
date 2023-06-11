# -*- coding: utf-8 -*-#
from typing import Any, Optional, Sequence, Tuple
from django.utils.translation import gettext as _

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
        self.attrs.update({"class": "relative"})
        # self.checked_attribute = ""
        # debugging_print(self.checked_attribute)
        # debugging_print(dir(self))


class BWEmailInput(forms.EmailInput):
    # template_name = "beach_wood_user/widgets/email.html"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize the widget here
        self.attrs["class"] = (
            f"py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 "
            f"focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400"
        )


class BWPasswordInput(forms.PasswordInput):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs["class"] = (
            f"py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 "
            f"focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400"
        )


class BWLoginForm(forms.Form):
    default_renderer = FormRenderer()
    user_type = forms.ChoiceField(
        label=False,
        choices=BeachWoodUserTypeEnum.choices,
        required=True,
        widget=BWUserTypeRadioSelect,
        error_messages={"required": _("User type required!")},
    )
    email = forms.EmailField(
        label="Email Address",
        required=True,
        widget=BWEmailInput,
        error_messages={"required": _("Email address required!")},
    )
    password = forms.CharField(
        widget=BWPasswordInput,
        required=True,
        error_messages={"required": _("Password required!")},
    )
