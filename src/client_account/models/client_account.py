# -*- coding: utf-8 -*-#
from django.db import models
from django.utils.translation import gettext as _

from core.choices import ClientAccountStatusEnum, ServiceNameEnum
from core.models.mixins import BaseModelMixin
from core.utils import PasswordHasher


from client.models import ClientProxy


class ClientAccount(BaseModelMixin):
    """Client account model related with client

    Args:
        BaseModelMixin (models.Model): Django base model mixin
    """

    client = models.ForeignKey(
        to=ClientProxy,
        on_delete=models.RESTRICT,
        null=True,
        related_name="client_accounts",
        blank=True,
    )
    is_services = models.BooleanField(_("is services"), default=False)
    account_name = models.CharField(_("account name"), max_length=50, null=True)
    account_email = models.EmailField(_("account email"), max_length=50, null=True)
    account_url = models.URLField(_("account url"), max_length=50, null=True)
    account_username = models.CharField(_("account username"), max_length=30, null=True)
    account_password = models.CharField(_("account password"), max_length=250, null=True)
    status = models.CharField(
        _("status"),
        max_length=10,
        choices=ClientAccountStatusEnum.choices,
        default=ClientAccountStatusEnum.ENABLED,
    )
    service_name = models.CharField(
        _("service name"),
        max_length=35,
        choices=ServiceNameEnum.choices,
        db_index=True,
        null=True,
        blank=True,
    )
    last_modified_date = models.DateTimeField(_("last_modified_date"), auto_now=True)

    def __str__(self) -> str:
        return f"{self.account_name}"

    # def get_absolute_url(self):
    #     return reverse("manager:client_account:details", kwargs={"pk": self.pk})

    @property
    def decrypted_account_password(self) -> str | None:
        if not self.account_password:
            return None
        else:
            # debugging_print(self.password)
            return PasswordHasher.decrypt(self.account_password)
