# -*- coding: utf-8 -*-#
from typing import Optional

from django import forms
from django.utils.translation import gettext as _

from beach_wood_user.helpers.permission_helper import PermissionHelper
from beach_wood_user.models import BWUser


class BWPermissionsForm(forms.Form):
    def __init__(self, staff_user: Optional[BWUser] = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.all_init_permissions = []
        self.all_initial_permissions = None
        self.all_initial_permissions_qs = PermissionHelper.get_bw_default_permissions(
            as_form_choices=True
        )

        # this field will create in __init__ method to prevent any problem for migration when init the project
        self.fields["permissions"] = forms.MultipleChoiceField(
            label=_("Permissions"),
            required=False,
            widget=forms.CheckboxSelectMultiple,
            choices=self.all_initial_permissions_qs,
            # queryset=self.all_initial_permissions_qs,
            # initial=self.all_init_permissions,
        )
        if staff_user is not None:
            for permissions in staff_user.user_permissions.all():
                self.all_init_permissions.append(permissions.pk)
            # debugging_print(self.all_init_permissions)
        self.fields.get("permissions").initial = self.all_init_permissions

    user = forms.UUIDField(widget=forms.HiddenInput)
