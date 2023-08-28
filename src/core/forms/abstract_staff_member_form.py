# -*- coding: utf-8 -*-#
from django import forms
from django.utils.translation import gettext as _

from core.choices import BeachWoodUserTypeEnum
from core.forms.widgets import RichHTMLEditorWidget, BWPasswordInputWidget


class AbstractStaffMemberForm(forms.Form):
    def __init__(self, user_type: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.get("user_type").initial = user_type

    field_order = ["first_name", "last_name", "email", "password", "confirm_password"]
    password = forms.CharField(
        label=_("Password"), required=True, widget=BWPasswordInputWidget
    )
    confirm_password = forms.CharField(
        label=_("Confirm Password"), required=True, widget=BWPasswordInputWidget
    )
    email = forms.EmailField(label=_("Email Address"), required=True)
    first_name = forms.CharField(label=_("First Name"), required=True)
    last_name = forms.CharField(label=_("Last Name"), required=True)
    profile_picture = forms.ImageField(label=_("Profile Picture"), required=False)
    address = forms.CharField(label=_("Address"), required=False)
    phone_number = forms.CharField(label=_("Phone number"), required=False)
    bio = forms.CharField(label=_("BIO"), widget=RichHTMLEditorWidget, required=False)
    user_type = forms.CharField(label="", widget=forms.HiddenInput, required=False)
    facebook = forms.URLField(label=_("Facebook"), required=False)
    twitter = forms.URLField(label=_("Twitter"), required=False)
    github = forms.URLField(label=_("Github"), required=False)
    linkedin = forms.URLField(label=_("Linkedin"), required=False)
    instagram = forms.URLField(label=_("Instagram"), required=False)

    class Meta:
        abstract = True

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError(_("Password confirmation not match!"), code="invalid")
        return confirm_password
