# -*- coding: utf-8 -*-#
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db import transaction
from django.utils.translation import gettext as _
from import_export.admin import ImportExportModelAdmin

from beach_wood_user.forms import BWUserCreationForm, BWUserChangeForm
from beach_wood_user.models import BWUser
from core.admin import BWBaseAdminModelMixin
from core.constants.users import READONLY_NEW_STAFF_MEMBER_GROUP_NAME
from core.utils.developments.debugging_print_object import BWDebuggingPrint


@admin.register(BWUser)
class BWUserAdmin(ImportExportModelAdmin, UserAdmin):
    actions = ["unset_readonly_group", "add_view_staffbriefcase_permission"]
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
    readonly_fields = ("date_joined", "last_login", "updated_at")
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
                    "updated_at",
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

    @admin.action(description=_("Add staff briefcase permissions for selected users"))
    def add_view_staffbriefcase_permission(self, request, queryset):
        try:

            if queryset:
                cnt = ContentType.objects.filter(
                    app_label="staff_briefcase",
                    model__in=[
                        "staffnotes",
                        "staffdocuments",
                        "staffaccounts",
                        "staffbriefcase",
                    ],
                )
                permissions = Permission.objects.filter(content_type__in=cnt)

                for qs in queryset:

                    qs.user_permissions.add(*list(permissions))
                    qs.save()
                self.message_user(
                    request,
                    _(
                        "View staffbriefcase permission added for selected users successfully"
                    ),
                    level=25,
                )
            else:
                self.message_user(
                    request,
                    _("Please select users to add view_staffbriefcase permission"),
                    level=20,
                )
        except Exception as ex:
            self.message_user(request, str(ex), level=40)

    @admin.action(description=_("Unset readonly group for selected users"))
    def unset_readonly_group(self, request, queryset):
        try:
            readonly_group = Group.objects.filter(
                name=READONLY_NEW_STAFF_MEMBER_GROUP_NAME
            )
            if not readonly_group:
                self.message_user(
                    request,
                    _("Readonly group not found"),
                    level="warning",
                )
                return
            readonly_group = readonly_group.first()
            with transaction.atomic():
                if queryset:
                    for qs in queryset:
                        if qs.groups.filter(pk=readonly_group.pk).exists() is True:
                            qs.groups.remove(readonly_group)
                            qs.save()
                    self.message_user(
                        request,
                        _("Readonly group unset for selected users successfully"),
                        level="success",
                    )
                else:
                    self.message_user(
                        request,
                        _("Please select users to unset readonly group"),
                        level="info",
                    )
        except Exception as ex:
            self.message_user(request, str(ex), level="error")
