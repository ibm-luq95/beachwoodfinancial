# -*- coding: utf-8 -*-#
from typing import Optional, Any

from bookkeeper.models import BookkeeperProxy


class InitBookkeeperRelatedFieldsMixin:
    """
    A mixin class that initializes fields related to a bookkeeper, such as clients, jobs,
    and tasks.
    """

    def __init__(
        self, bookkeeper: Optional[BookkeeperProxy] = None, *args: Any, **kwargs: Any
    ) -> None:
        """
        Initializes the InitBookkeeperRelatedFieldsMixin instance.

        Args:
            bookkeeper: An optional BookkeeperProxy instance. Defaults to None.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        """
        if "client" in self.fields:
            self.fields["client"].queryset = self.fields["client"].queryset.order_by(
                "name"
            )
        if "job" in self.fields:
            self.fields["job"].queryset = self.fields["job"].queryset.order_by("title")
        if "task" in self.fields:
            self.fields["task"].queryset = self.fields["task"].queryset.order_by("title")

        if bookkeeper is not None:
            if self.fields.get("client") is not None:
                self.fields["client"].queryset = bookkeeper.get_proxy_model().clients.all()
            if self.fields.get("job") is not None:
                self.fields["job"].queryset = bookkeeper.get_proxy_model().get_user_jobs()
            if self.fields.get("task") is not None:
                self.fields["task"].queryset = (
                    bookkeeper.get_proxy_model().get_all_related_items("tasks")
                )
