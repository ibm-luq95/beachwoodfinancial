from __future__ import annotations

from typing import Any
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils.translation import gettext_lazy as _

from core.models.mixins import BaseModelMixin

class NotificationVerb(models.TextChoices):
    CREATED = "created", _("Created")
    UPDATED = "updated", _("Updated")
    DELETED = "deleted", _("Deleted")
    ASSIGNED = "assigned", _("Assigned")
    COMMENTED = "commented", _("Commented")
    STATUS_CHANGED = "status_changed", _("Status Changed")

class Notification(BaseModelMixin):
    actor = models.ForeignKey(
        to="beach_wood_user.BWUser",
        on_delete=models.SET_NULL,
        related_name="triggered_notifications",
        null=True,
        blank=True,
    )
    verb = models.CharField(
        max_length=20,
        choices=NotificationVerb.choices,
        default=NotificationVerb.CREATED,
    )
    message_template = models.TextField(
        _("message template"),
        help_text=_("Template string or final message text"),
    )
    content_type = models.ForeignKey(
        to=ContentType,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    object_id = models.UUIDField(
        null=True,
        blank=True,
    )
    content_object = GenericForeignKey("content_type", "object_id")

    class Meta(BaseModelMixin.Meta):
        ordering = ["-created_at"]
        verbose_name = _("notification")
        verbose_name_plural = _("notifications")
        db_table = "lf_notifications_notification"
        indexes = [
            models.Index(fields=["content_type", "object_id"], name="lf_notification_gfk_idx"),
        ]

    def __str__(self) -> str:
        return f"{self.actor} - {self.verb}"

    def get_absolute_url(self) -> str:
        if self.content_object and hasattr(self.content_object, "get_absolute_url"):
            return self.content_object.get_absolute_url()
        return "#"

class NotificationProxy(Notification):
    class Meta(Notification.Meta):
        proxy = True
