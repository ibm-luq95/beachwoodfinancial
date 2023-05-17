# -*- coding: utf-8 -*-#
from django.conf import settings
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext as _

from core.constants.file_types_validation import IMAGES_FT
from core.constants.status_labels import CON_ARCHIVED
from core.utils import FileValidator
from core.utils import get_trans_txt

file_validator = FileValidator(
    max_size=1024 * 1000,
    content_types=IMAGES_FT,
)


class StaffMemberMixin(models.Model):
    user = models.OneToOneField(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="%(class)s"
    )
    profile_picture = models.ImageField(
        _("profile picture"), upload_to="profile_pictures/", null=True, blank=True, validators=[file_validator]
    )

    bio = models.TextField(_("bio"), null=True, blank=True)

    class Meta:
        abstract = True

    @property
    def is_active_labeled(self) -> str:
        if self.user.is_active is True:
            return get_trans_txt("Active")
        else:
            return get_trans_txt("Deactivate")

    def get_not_seen_special_assignments(self):
        if hasattr(self, "special_assignments"):
            return self.special_assignments.filter(
                Q(is_seen=False) & ~Q(status__in=[CON_ARCHIVED])
            )
        else:
            None
