# -*- coding: utf-8 -*-#
from typing import Optional

from django import forms
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext as _

from beach_wood_user.models import BWUser
from core.constants.users import DEFAULT_PERMISSIONS_NEW_STAFF_MEMBER
from core.utils import debugging_print

all_initial_permissions = None
all_content_types = []
for content_type_item in DEFAULT_PERMISSIONS_NEW_STAFF_MEMBER:
    content_type_object = ContentType.objects.get(
        app_label=content_type_item["app_label"], model=content_type_item["model_label"]
    )
    all_content_types.append(content_type_object)
all_initial_permissions = Permission.objects.filter(content_type__in=all_content_types)


class BWPermissionsForm(forms.Form):
    def __init__(self, staff_user: Optional[BWUser] = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.all_init_permissions = []
        if staff_user is not None:
            for group in staff_user.groups.all():
                permissions = group.permissions.all()
                if permissions:
                    for permission in permissions:
                        self.all_init_permissions.append(permission)
            # debugging_print(self.all_init_permissions)
            self.fields.get("permissions").initial = self.all_init_permissions

    permissions = forms.ModelMultipleChoiceField(
        label=_("Permissions"),
        queryset=all_initial_permissions,
        required=False,
        widget=forms.CheckboxSelectMultiple,
    )
    user = forms.UUIDField(widget=forms.HiddenInput)