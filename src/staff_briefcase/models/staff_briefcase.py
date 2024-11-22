# -*- coding: utf-8 -*-#
from django.utils.translation import gettext as _
from django.db import models

from beach_wood_user.models import BWUser
from core.models.mixins import BaseModelMixin
from staff_briefcase.models import StaffAccounts
from staff_briefcase.models.documents import StaffDocuments
from staff_briefcase.models.notes import StaffNotes


class StaffBriefcase(BaseModelMixin):
    """Represents a briefcase for staff members.

    This class defines a briefcase for staff members to store notes, documents, and accounts.

    Attributes:
        user (OneToOneField): A one-to-one relationship to the `BWUser` model representing the user associated with the briefcase.
        notes (ManyToManyField): A many-to-many relationship to the `StaffNotes` model for storing notes in the briefcase.
        documents (ManyToManyField): A many-to-many relationship to the `StaffDocuments` model for storing documents in the briefcase.
        accounts (ManyToManyField): A many-to-many relationship to the `StaffAccounts` model for storing accounts in the briefcase.
    """

    user = models.OneToOneField(
        to=BWUser, related_name="briefcase", on_delete=models.CASCADE
    )
    notes = models.ManyToManyField(to=StaffNotes, related_name="briefcase", blank=True)
    documents = models.ManyToManyField(
        to=StaffDocuments, related_name="briefcase", blank=True
    )
    accounts = models.ManyToManyField(
        to=StaffAccounts, related_name="briefcase", blank=True
    )

    class Meta(BaseModelMixin.Meta):
        verbose_name = _("Staff Briefcase")
        verbose_name_plural = _("Staff Briefcases")
        indexes = [
            models.Index(name="briefcase_staff_user_idx", fields=["user"]),
        ]

    def __str__(self):
        return _(f"Briefcase for - {self.user}")
