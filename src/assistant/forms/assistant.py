# -*- coding: utf-8 -*-#
from typing import Optional
from uuid import UUID

from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _

from django import forms

from core.choices import AssistantTypeEnum
from core.constants.users import CON_ASSISTANT
from core.forms import AbstractStaffMemberForm

ASSISTANT_TYPE_TEXT = (
    _(f"If assistant type is ")
    + "<strong class='d-inline-block px-1'>ADMIN</strong>"
    + _("the assistant user will have manager permissions")
)


class AssistantForm(AbstractStaffMemberForm):
    STAFF_MEMBER_TYPE = CON_ASSISTANT
    field_order = AbstractStaffMemberForm.field_order + ["assistant_type"]

    assistant_type = forms.ChoiceField(
        choices=AssistantTypeEnum.choices, help_text=mark_safe(ASSISTANT_TYPE_TEXT)
    )

    def __init__(
        self, user_type: Optional[str] = None, pk: Optional[UUID] = None, *args, **kwargs
    ):
        # super(BookkeeperForm, self).__init__(*args, **kwargs)
        super().__init__(user_type=self.STAFF_MEMBER_TYPE, *args, **kwargs)
