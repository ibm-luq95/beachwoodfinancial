# -*- coding: utf-8 -*-#
from django import forms
from django.forms import ValidationError
from django.utils.translation import gettext as _

from core.forms.widgets import BWPasswordInputWidget
from core.utils import get_trans_txt


class ForceChangePasswordForm(forms.Form):
    password1 = forms.CharField(label=get_trans_txt("Password"), widget=BWPasswordInputWidget)
    password2 = forms.CharField(
        label=get_trans_txt("Password confirmation"), widget=BWPasswordInputWidget
    )

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(_("Passwords not match"))
        return password2
