# -*- coding: utf-8 -*-#
from core.constants.users import CON_BOOKKEEPER


class BookkeeperPassRelatedMixin:
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user.user_type == CON_BOOKKEEPER:
            kwargs.update({"bookkeeper": self.request.user.bookkeeper})
        return kwargs
