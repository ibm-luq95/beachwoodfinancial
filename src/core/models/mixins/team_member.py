# -*- coding: utf-8 -*-#
from assistant.models import Assistant
from bookkeeper.models import BookkeeperProxy
from django.db import models
from manager.models import Manager

from core.models.fields import CustomForeignKey


class TeamMembersMixin(models.Model):
    assistant = CustomForeignKey(
        to=Assistant,
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
        to=Manager,
        on_delete=models.PROTECT,
        related_name="%(class)s",
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True

    def get_managed_user(self):
        if self.bookkeeper:
            return self.bookkeeper
        elif self.assistant:
            return self.assistant
        elif self.manager:
            return self.manager
        else:
            return None

    @property
    def get_user_type(self):
        return self.get_managed_user().user.user_type
