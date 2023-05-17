# -*- coding: utf-8 -*-#
from django import forms
from core.choices import BeachWoodUserTypeEnum


class BWLoginForm(forms.Form):
    user_type = forms.ChoiceField(
        label="User Type", choices=BeachWoodUserTypeEnum.choices, required=True
    )
    email = forms.EmailField(label="Email Address", required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
