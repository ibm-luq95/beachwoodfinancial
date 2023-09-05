# -*- coding: utf-8 -*-#
from typing import Optional
from uuid import UUID
from django.utils.safestring import mark_safe
from django import forms
from django.utils.translation import gettext as _

from core.constants.users import CON_MANAGER
from core.forms import AbstractStaffMemberForm

IS_SUPERUSER_HELP = (
    "<strong>" + _("The manager will have full administrator permissions") + "</strong>"
)


class ManagerForm(AbstractStaffMemberForm):
    field_order = ["first_name", "last_name", "email", "is_superuser"]
    STAFF_MEMBER_TYPE = CON_MANAGER

    is_superuser = forms.BooleanField(
        label=_("Is superuser"), help_text=mark_safe(IS_SUPERUSER_HELP), required=False
    )

    def __init__(
        self, user_type: Optional[str] = None, pk: Optional[UUID] = None, *args, **kwargs
    ):
        # super(BookkeeperForm, self).__init__(*args, **kwargs)
        super().__init__(user_type=self.STAFF_MEMBER_TYPE, *args, **kwargs)
