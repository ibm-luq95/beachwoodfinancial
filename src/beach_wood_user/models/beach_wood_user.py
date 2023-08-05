# -*- coding: utf-8 -*-#
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models, transaction
from django.utils import timezone
from django.utils.translation import gettext as _

from core.choices import (
    BeachWoodUserTypeEnum,
    BeachWoodUserStatusEnum,
    BeachWoodUserTypesEnum,
)
from core.models.mixins import BaseModelMixin
from core.utils import get_formatted_logger
from .manager import BeachWoodUserManager

# TODO: remove the custom logger before push (only for development)
# ###### [Custom Logger] #########
logger = get_formatted_logger()


# ###### [Custom Logger] #########


class BWUser(BaseModelMixin, AbstractBaseUser, PermissionsMixin):
    """BWUser, it used instead of default django user model

    Args:
        BaseModelMixin (_type_): _description_
        AbstractBaseUser (_type_): _description_
        PermissionsMixin (_type_): _description_

    Returns:
        _type_: _description_
    """

    first_name = models.CharField(_("first name"), max_length=15)
    last_name = models.CharField(_("last name"), max_length=15)
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(_("is staff"), default=False)
    is_active = models.BooleanField(_("is active"), default=True)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    user_type = models.CharField(
        _("user type"), choices=BeachWoodUserTypeEnum.choices, max_length=15
    )
    status = models.CharField(
        _("status"),
        max_length=10,
        choices=BeachWoodUserStatusEnum.choices,
        default=BeachWoodUserStatusEnum.ENABLED,
    )
    user_genre = models.CharField(
        _("user genre"),
        max_length=10,
        choices=BeachWoodUserTypesEnum.choices,
        default=BeachWoodUserTypesEnum.USER,
        db_index=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["user_type", "user_genre"]

    objects = BeachWoodUserManager()

    class Meta:
        verbose_name = _("Beach wood user")
        verbose_name_plural = _("Beach wood users")
        ordering = ["-created_at", "-updated_at"]
        permissions = [("developer_user", "Developer User")]

    def __str__(self):
        full_info = self.fullname
        return full_info

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
