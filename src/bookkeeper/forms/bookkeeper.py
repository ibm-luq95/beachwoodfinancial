# -*- coding: utf-8 -*-#
from typing import Optional
from uuid import UUID

from bookkeeper.models import BookkeeperProxy
from core.constants.users import CON_BOOKKEEPER
from core.forms import AbstractStaffMemberForm


class BookkeeperForm(AbstractStaffMemberForm):
    STAFF_MEMBER_TYPE = CON_BOOKKEEPER

    def __init__(
        self, user_type: Optional[str] = None, pk: Optional[UUID] = None, *args, **kwargs
    ):
        # super(BookkeeperForm, self).__init__(*args, **kwargs)
        super().__init__(user_type=self.STAFF_MEMBER_TYPE, *args, **kwargs)

        # if pk is not None:
        #     bookkeeper = BookkeeperProxy.objects.get(pk=pk)
        #     self.fields.get("bio").initial = bookkeeper.bio
        #     self.fields.get("first_name").initial = bookkeeper.user.first_name
        #     self.fields.get("last_name").initial = bookkeeper.user.last_name
        #     self.fields.get("email").initial = bookkeeper.user.email
        #     self.fields.get("profile_picture").initial = bookkeeper.profile_picture
