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
    """A form for creating or updating an Assistant.

    This form extends the `AbstractStaffMemberForm` and adds additional fields specific to an Assistant.

    Attributes:
        STAFF_MEMBER_TYPE (str): The type of staff member. It is set to `CON_ASSISTANT`.
        field_order (list): The order of fields in the form. It includes the fields from `AbstractStaffMemberForm`
            and appends "assistant_type".
        assistant_type (forms.ChoiceField): A choice field for selecting the assistant type.
            It has choices defined in the `AssistantTypeEnum` enum.

    Methods:
        __init__(self, user_type: Optional[str] = None, pk: Optional[UUID] = None, *args, **kwargs):
            Initializes the form with the given parameters. It calls the parent's `__init__` method
            with the `user_type` set to `STAFF_MEMBER_TYPE` and the other parameters.
    """

    STAFF_MEMBER_TYPE = CON_ASSISTANT
    field_order = AbstractStaffMemberForm.field_order + ["assistant_type"]

    assistant_type = forms.ChoiceField(
        choices=AssistantTypeEnum.choices, help_text=mark_safe(ASSISTANT_TYPE_TEXT)
    )

    def __init__(
        self, user_type: Optional[str] = None, pk: Optional[UUID] = None, *args, **kwargs
    ):
        """Initializes the AssistantForm.

        Args:
            user_type (str, optional): The type of user. Defaults to None.
            pk (UUID, optional): The primary key of the Assistant. Defaults to None.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        # super(BookkeeperForm, self).__init__(*args, **kwargs)
        super().__init__(user_type=self.STAFF_MEMBER_TYPE, *args, **kwargs)
