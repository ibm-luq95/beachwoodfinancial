# -*- coding: utf-8 -*-#
from django.urls import reverse_lazy

from core.choices import (
    BeachWoodUserStatusEnum,
    BeachWoodUserTypeEnum,
    BeachWoodUserTypesEnum,
)
from core.models.mixins import BaseModelMixin
from core.utils import get_formatted_logger
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from guardian.mixins import GuardianUserMixin

from .manager import BeachWoodUserManager

# TODO: remove the custom logger before push (only for development)
# ###### [Custom Logger] #########
logger = get_formatted_logger()


# ###### [Custom Logger] #########


class BWUser(BaseModelMixin, AbstractBaseUser, PermissionsMixin, GuardianUserMixin):
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

    def __str__(self) -> str:
        full_info = self.fullname
        if full_info != "":
            return f"User - {full_info}"
        else:
            return f"User - {self.email}"

    @property
    def fullname(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs) -> None:
        self.email = self.email.lower()
        super(BWUser, self).save(*args, **kwargs)

    @property
    def get_staff_member_object(self) -> dict:
        user_dict = dict()
        user_dict["user_type"] = self.user_type
        if hasattr(self, "bookkeeper"):
            # user_dict["staff_object"] = getattr(self, "bookkeeper")
            user_dict["staff_object"] = getattr(self, "bookkeeper")
        elif hasattr(self, "manager"):
            user_dict["staff_object"] = getattr(self, "manager")
        elif hasattr(self, "assistant"):
            user_dict["staff_object"] = getattr(self, "assistant")

        return user_dict

    def get_staff_details(self) -> dict:
        user_dict = dict()
        staff_object = self.get_staff_member_object.get("staff_object")
        user_dict.update(
            {
                "linkedin": getattr(staff_object.profile, "linkedin", None),
                "instagram": getattr(staff_object.profile, "instagram", None),
                "github": getattr(staff_object.profile, "github", None),
                "profile_picture": getattr(staff_object.profile, "profile_picture", None),
                "facebook": getattr(staff_object.profile, "facebook", None),
                "twitter": getattr(staff_object.profile, "twitter", None),
                "bio": getattr(staff_object.profile, "bio", None),
                "first_name": self.first_name,
                "last_name": self.last_name,
                "email": self.email,
                "phone_number": getattr(staff_object.profile, "phone_number", None),
                "address": getattr(staff_object.profile, "address", None),
            }
        )
        if self.user_type == "assistant":
            user_dict.update(
                {
                    "assistant_type": self.get_staff_member_object.get(
                        "staff_object"
                    ).assistant_type
                }
            )
        if self.user_type == "manager":
            user_dict.update({"is_superuser": self.is_superuser})
        return user_dict

    def get_absolute_url(self):
        return reverse_lazy("dashboard:staff:member-details", kwargs={"pk": self.pk})
