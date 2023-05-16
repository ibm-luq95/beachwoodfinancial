# -*- coding: utf-8 -*-#
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext as _

from core.constants.status_labels import CON_ARCHIVED
from core.utils import get_trans_txt


class StaffMemberMixin(models.Model):
    user = models.OneToOneField(
        to=get_user_model(), on_delete=models.CASCADE, related_name="%(class)s"
    )
    profile_picture = models.ImageField(
        _("profile picture"), upload_to="profile_pictures/", null=True, blank=True
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
        return self.special_assignments.filter(
            Q(is_seen=False) & ~Q(status__in=[CON_ARCHIVED])
        )
