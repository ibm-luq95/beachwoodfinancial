# -*- coding: utf-8 -*-#
from PIL import Image
from django.db import models
from django.utils.translation import gettext as _

from core.constants.file_types_validation import IMAGES_FT
from core.models.mixins import BaseModelMixin
from core.models.mixins.staff_member_social_media import StaffMemberSocialMediaMixin
from core.utils import FileValidator

file_validator = FileValidator(max_size=1024 * 1000, content_types=IMAGES_FT)


class Profile(BaseModelMixin, StaffMemberSocialMediaMixin, models.Model):
    profile_picture = models.ImageField(
        _("profile picture"),
        upload_to="profile_pictures/",
        null=True,
        blank=True,
        validators=[file_validator],
    )
    address = models.CharField(_("address"), max_length=50, null=True, blank=True)
    phone_number = models.CharField(
        _("phone number"), max_length=50, null=True, blank=True
    )
    bio = models.TextField(_("bio"), null=True, blank=True)

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        if self.profile_picture:
            image = Image.open(self.profile_picture.path)
            if image.height > 120 or image.width > 120:
                output_size = (120, 120)
                image.thumbnail(output_size)
                image.save(self.profile_picture.path)
