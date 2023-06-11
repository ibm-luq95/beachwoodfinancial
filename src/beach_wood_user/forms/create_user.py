# -*- coding: utf-8 -*-#
from django.contrib.auth.forms import UserCreationForm

from beach_wood_user.models import BWUser


class BWUserCreationForm(UserCreationForm):
    class Meta:
        model = BWUser
        fields = (
            "email",
            "first_name",
            "last_name",
            "user_type",
            "password",
        )
