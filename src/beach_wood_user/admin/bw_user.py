# -*- coding: utf-8 -*-#
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext as _

from beach_wood_user.forms import BWUserCreationForm, BWUserChangeForm
from beach_wood_user.models import BWUser
from core.admin import BWBaseAdminModelMixin


@admin.register(BWUser)
class BWUserAdmin(UserAdmin):
    add_form = BWUserCreationForm
    form = BWUserChangeForm
    ordering = ("email",)
    model = BWUser
    list_filter = [
        "user_type",
        "is_active",
        "is_superuser",
    ] + BWBaseAdminModelMixin.list_filter
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
    readonly_fields = ("date_joined", "last_login")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "user_type",
                    "status",
                    "user_genre",
                )
            },
        ),
        (
            _("Permissions"),
            {"fields": ("is_staff", "is_active", "groups", "user_permissions")},
        ),
        (
            _("Activity"),
            {
                "fields": (
                    "date_joined",
                    "last_login",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            _("User credentials"),
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    # "user_type",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
        (
            _("Permissions"),
            {
                "classes": ("wide",),
                "fields": (
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "user_type",
                    "status",
                    "user_genre",
                )
            },
        ),
    )
    search_fields = ("email", "first_name", "last_name")
