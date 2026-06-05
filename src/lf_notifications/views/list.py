from __future__ import annotations

from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from lf_notifications.models import NotificationRecipientProxy

class NotificationListView(LoginRequiredMixin, ListView):
    model = NotificationRecipientProxy
    template_name = "lf_notifications/list.html"
    context_object_name = "notifications"
    paginate_by = 20

    def get_queryset(self):
        return NotificationRecipientProxy.objects.filter(
            recipient=self.request.user
        ).select_related(
            "notification", 
            "notification__actor", 
            "notification__content_type"
        ).prefetch_related(
            "notification__actor__bookkeeper__profile",
            "notification__actor__manager__profile",
            "notification__actor__assistant__profile",
            "notification__actor__cfo__profile",
        ).order_by("-created_at")
