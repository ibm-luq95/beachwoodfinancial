# -*- coding: utf-8 -*-#
from django.db import models
from django.utils.translation import gettext as _

from core.choices import ServiceNameEnum
from core.models.mixins import BaseModelMixin
from core.models.mixins import StrModelMixin
from core.utils import PasswordHasher


class StaffAccounts(BaseModelMixin, StrModelMixin):
    title = models.CharField(_("title"), max_length=25)
    url = models.URLField(_("url"), null=True, blank=True)
    username_email = models.CharField(_("Username / Email"), max_length=100)
    password = models.CharField(_("Password"), max_length=250)
    name = models.CharField(
        _("name"),
        max_length=35,
        choices=ServiceNameEnum.choices,
        null=True,
        blank=True,
    )

    class Meta(BaseModelMixin.Meta):
        indexes = [
            models.Index(name="staff_account_name_idx", fields=["name"]),
            models.Index(name="staff_account_title_idx", fields=["title"]),
            models.Index(name="staff_account_username_idx", fields=["username_email"]),
        ]

    @property
    def decrypted_password(self) -> str | None:
        """
        Property function to return the decrypted password if it exists, otherwise returns None.
        """
        if not self.password:
            return None
        else:
            return PasswordHasher.decrypt(self.password)

    def save(self, *args, **kwargs):
        if self.decrypted_password:
            self.account_password = PasswordHasher.encrypt(self.password)
        else:
            self.account_password = PasswordHasher.encrypt(self.account_password)
        super(StaffAccounts, self).save(*args, **kwargs)
