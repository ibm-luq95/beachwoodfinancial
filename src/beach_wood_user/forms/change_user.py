# -*- coding: utf-8 -*-#
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserChangeForm

from beach_wood_user.models import BWUser


class BWUserChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    # password = ReadOnlyPasswordHashField()

    class Meta:
        model = BWUser
        fields = "__all__"
