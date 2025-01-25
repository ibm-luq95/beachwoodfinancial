# -*- coding: utf-8 -*-#
from django.contrib import admin

from beach_wood_user.models import Profile
from core.admin import BWBaseAdminModelMixin


@admin.register(Profile)
class ProfileAdmin(BWBaseAdminModelMixin):
    # list_display = ["address"]
    pass
