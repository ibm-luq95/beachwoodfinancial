# -*- coding: utf-8 -*-#
from django.conf import settings
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext as _

from beach_wood_user.models.profile import Profile
from core.constants.status_labels import CON_ARCHIVED
from core.models.querysets import BaseQuerySetMixin


class StaffMemberMixin(models.Model):
	user = models.OneToOneField(
		to=settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		related_name="%(class)s",
		null=True,
		blank=True,
	)
	profile = models.OneToOneField(
		to=Profile,
		on_delete=models.CASCADE,
		related_name="%(class)s",
		null=True,
		blank=True,
	)

	def __str__(self) -> str:
		# return f"Assistant - {self.user.first_name} {self.user.last_name}"
		return f"{self.user.fullname}"

	class Meta:
		ordering = ["user__first_name"]
		abstract = True

	@property
	def is_active_labeled(self) -> str:
		if self.user.is_active is True:
			return _("Active")
		else:
			return _("Deactivate")

	def get_not_seen_special_assignments(self) -> BaseQuerySetMixin | None:
		if hasattr(self, "special_assignments"):
			return self.special_assignments.filter(
				Q(is_seen=False) & ~Q(status__in=[CON_ARCHIVED])
			)
		else:
			return None
