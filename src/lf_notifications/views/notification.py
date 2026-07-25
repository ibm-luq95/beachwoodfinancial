from __future__ import annotations

from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone

from lf_notifications.models import NotificationRecipientProxy
from lf_notifications.serializers.notification import NotificationRecipientSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationRecipientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Ensure users can only see their own notifications.
        """
        return NotificationRecipientProxy.objects.filter(
            recipient=self.request.user
        ).select_related("notification", "notification__actor", "notification__content_type")

    @action(detail=True, methods=["post"])
    def mark_read(self, request, pk=None):
        notification_recipient = self.get_object()
        notification_recipient.mark_as_read()
        return Response({"status": "notification marked as read"})

    @action(detail=False, methods=["post"])
    def mark_all_read(self, request):
        self.get_queryset().filter(is_read=False).update(
            is_read=True, 
            read_at=timezone.now()
        )
        return Response({"status": "all notifications marked as read"})

    @action(detail=False, methods=["get"])
    def unread_count(self, request):
        count = self.get_queryset().filter(is_read=False).count()
        return Response({"unread_count": count})
