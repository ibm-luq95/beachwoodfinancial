# -*- coding: utf-8 -*-#
from django.contrib import admin

from beach_wood_user.models import BWUser
from core.admin import BWBaseAdminModelMixin


@admin.register(BWUser)
class BWUserAdmin(BWBaseAdminModelMixin):
    list_filter = ["user_type", "is_active", "is_superuser"] + BWBaseAdminModelMixin.list_filter
    list_display = (
        "email",
        "first_name",
        "last_name",
        "user_type",
        "user_genre",
        "is_active",
        "last_login",
        "created_at",
    )
