# -*- coding: utf-8 -*-#
from core.constants.users import CON_BOOKKEEPER


class BookkeeperPassRelatedMixin:
    """
    Mixin class that provides form kwargs for bookkeeper-related actions.

    Methods:
        get_form_kwargs() -> dict: Retrieves the form kwargs for bookkeeper-related actions.

    """

    def get_form_kwargs(self):
        """
        Retrieves the form kwargs for bookkeeper-related actions.

        Returns:
            dict: The form kwargs with the bookkeeper information if the user is a bookkeeper.

        """
        kwargs = super().get_form_kwargs()
        if self.request.user.user_type == CON_BOOKKEEPER:
            kwargs.update({"bookkeeper": self.request.user.bookkeeper})
        return kwargs
