# -*- coding: utf-8 -*-#
from assistant.models import AssistantProxy
from bookkeeper.models import BookkeeperProxy
from django.db import models
from manager.models import ManagerProxy

from core.models.fields import CustomForeignKey


class TeamMembersMixin(models.Model):
    """
    A mixin class for team members.

    This class provides functionality for managing team members in a system. It includes fields for associating team members with assistant, bookkeeper, and manager roles. The `get_managed_user` method returns the user associated with the team member based on their role. The `get_user_type` property returns the user type of the managed user.

    Attributes:
        assistant (CustomForeignKey): A foreign key to the AssistantProxy model representing the assistant role.
        bookkeeper (CustomForeignKey): A foreign key to the BookkeeperProxy model representing the bookkeeper role.
        manager (CustomForeignKey): A foreign key to the ManagerProxy model representing the manager role.

    Methods:
        get_managed_user(): Returns the user associated with the team member based on their role.
        get_user_type(): Returns the user type of the managed user.

    """

    assistant = CustomForeignKey(
        to=AssistantProxy,
        on_delete=models.PROTECT,
        related_name="%(class)s",
        null=True,
        blank=True,
    )
    bookkeeper = CustomForeignKey(
        to=BookkeeperProxy,
        on_delete=models.PROTECT,
        related_name="%(class)s",
        null=True,
        blank=True,
    )
    manager = CustomForeignKey(
        to=ManagerProxy,
        on_delete=models.PROTECT,
        related_name="%(class)s",
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True

    def get_managed_user(self):
        """
        Returns the user associated with the team member based on their role.

        This method checks the role of the team member and returns the corresponding user.
        The role is determined by the presence of the 'bookkeeper', 'assistant', or 'manager' attributes.

        Returns:
            The user associated with the team member based on their role.
            Returns None if the team member does not have any of the role attributes.

        """
        if self.bookkeeper:
            return self.bookkeeper
        elif self.assistant:
            return self.assistant
        elif self.manager:
            return self.manager
        else:
            return None

    @property
    def get_user_type(self) -> str:
        """
        Get the user type of the managed user.

        Returns:
            str: The user type of the managed user.

        """
        return self.get_managed_user().user.user_type
