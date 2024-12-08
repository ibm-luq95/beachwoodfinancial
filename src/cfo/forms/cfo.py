# -*- coding: utf-8 -*-#
from typing import Optional
from uuid import UUID

from core.constants.users import CON_CFO
from core.forms import AbstractStaffMemberForm


class CFOForm(AbstractStaffMemberForm):
    STAFF_MEMBER_TYPE = CON_CFO

    def __init__(
        self, user_type: Optional[str] = None, pk: Optional[UUID] = None, *args, **kwargs
    ):
        # super(BookkeeperForm, self).__init__(*args, **kwargs)
        super().__init__(user_type=self.STAFF_MEMBER_TYPE, *args, **kwargs)
