from django.db import models
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet

from core.api.permissions import BaseApiPermissionMixin
from core.api.mixins import RoleScopedQuerysetMixin
from core.utils import get_formatted_logger
from task.models import TaskProxy
from task.serializers import TaskSerializer

logger = get_formatted_logger()


class TaskViewSet(RoleScopedQuerysetMixin, ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated, BaseApiPermissionMixin)
    perm_slug = "task.task"
    authentication_classes = [TokenAuthentication]
    queryset = TaskProxy.objects.all()

    def scope_queryset_for_bookkeeper(self, queryset, bookkeeper):
        return queryset.filter(
            models.Q(job__managed_by=bookkeeper.user) |
            models.Q(job__bookkeeper=bookkeeper) |
            models.Q(job__client__bookkeepers=bookkeeper)
        )

    def scope_queryset_for_cfo(self, queryset, cfo):
        return queryset.filter(job__client__cfos=cfo)
