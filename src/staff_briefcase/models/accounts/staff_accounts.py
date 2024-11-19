# -*- coding: utf-8 -*-#
from django.db import models
from django.utils.translation import gettext as _

from core.choices import ServiceNameEnum
from core.models.mixins import BaseModelMixin
from core.models.mixins import StrModelMixin
from core.utils import PasswordHasher


class StaffAccounts(BaseModelMixin, StrModelMixin):
    """Represents a staff account.

    This class defines a staff account with attributes such as title, URL, username/email, password, and name.

    Attributes:
        title (CharField): The title of the account.
        url (TextField): The URL associated with the account.
        username_email (CharField): The username or email associated with the account.
        password (CharField): The password associated with the account.
        name (CharField): The name of the service associated with the account.

    Methods:
        decrypted_password(self) -> str | None: Returns the decrypted password if it exists, otherwise returns None.
        save(self, *args, **kwargs): Overrides the save method to encrypt the password before saving.
    """

    title = models.CharField(_("title"), max_length=25)
    url = models.TextField(_("url"), null=True, blank=True)
    username_email = models.CharField(_("Username / Email"), max_length=150)
    password = models.CharField(_("Password"), max_length=250)
    name = models.CharField(
        _("name"),
        max_length=35,
        choices=ServiceNameEnum.choices,
        null=True,
        blank=True,
    )

    class Meta(BaseModelMixin.Meta):
        ordering = ["title"]
        indexes = [
            models.Index(name="staff_account_name_idx", fields=["name"]),
            models.Index(name="staff_account_title_idx", fields=["title"]),
            models.Index(name="staff_account_username_idx", fields=["username_email"]),
        ]

    @property
    def decrypted_password(self) -> str | None:
        """Property function to return the decrypted password if it exists, otherwise
        returns None."""
        if not self.password:
            return None
        else:
            return PasswordHasher.decrypt(self.password)

    def save(self, *args, **kwargs):
        if self.decrypted_password:
            self.password = PasswordHasher.encrypt(self.password)
        else:
            self.password = PasswordHasher.encrypt(self.password)
        super(StaffAccounts, self).save(*args, **kwargs)
