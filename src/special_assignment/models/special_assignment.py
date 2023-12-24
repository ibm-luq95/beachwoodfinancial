# -*- coding: utf-8 -*-#
from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _

from client.models import ClientProxy
from core.choices.special_assignment import SpecialAssignmentStatusEnum
from core.constants.file_types_validation import IMAGES_AND_DOCS_FT
from core.models.mixins import (
    BaseModelMixin,
    StartAndDueDateMixin,
    TeamMembersMixin,
    StrModelMixin,
)
from core.models.mixins.cron_column_mixin import CronColumnMixin
from core.utils import FileValidator
from job.models import JobProxy
from special_assignment.models.manager import SpecialAssignmentsManager

file_validator = FileValidator(max_size=1024 * 1000, content_types=IMAGES_AND_DOCS_FT)


class SpecialAssignment(
    BaseModelMixin, StartAndDueDateMixin, TeamMembersMixin, CronColumnMixin, StrModelMixin
):
    client = models.ForeignKey(
        to=ClientProxy,
        on_delete=models.PROTECT,
        related_name="special_assignments",
        null=True,
        blank=True,
        db_index=True,
    )
    job = models.ForeignKey(
        to=JobProxy,
        on_delete=models.PROTECT,
        related_name="special_assignments",
        null=True,
        blank=True,
        db_index=True,
    )
    title = models.CharField(_("title"), max_length=100, null=False, blank=False)
    body = models.TextField(_("body"))
    status = models.CharField(
        _("status"),
        max_length=15,
        choices=SpecialAssignmentStatusEnum.choices,
        default=SpecialAssignmentStatusEnum.NOT_STARTED,
        db_index=True,
    )
    attachment = models.FileField(
        _("attachment"),
        upload_to="special_assignment_attachments/",
        null=True,
        blank=True,
        validators=[file_validator],
    )
    notes = models.TextField(_("notes"), null=True, blank=True)
    is_seen = models.BooleanField(_("is seen"), default=False, db_index=True)
    assigned_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="requested_assignments",
        help_text=_("readonly, you cant modified it"),
        editable=False,
        null=True,
        blank=True,
        db_index=True,
    )

    objects = SpecialAssignmentsManager()

    class Meta(BaseModelMixin.Meta):
        ordering = ["title"]
