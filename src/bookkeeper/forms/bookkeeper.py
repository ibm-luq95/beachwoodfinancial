# -*- coding: utf-8 -*-#
from typing import Optional
from uuid import UUID

from core.constants.users import CON_BOOKKEEPER
from core.forms import AbstractStaffMemberForm


class BookkeeperForm(AbstractStaffMemberForm):
    STAFF_MEMBER_TYPE = CON_BOOKKEEPER

    def __init__(
        self, user_type: Optional[str] = None, pk: Optional[UUID] = None, *args, **kwargs
    ):
        # super(BookkeeperForm, self).__init__(*args, **kwargs)
        super().__init__(user_type=self.STAFF_MEMBER_TYPE, *args, **kwargs)
