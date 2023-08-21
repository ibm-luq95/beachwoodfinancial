# -*- coding: utf-8 -*-#
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from client.models import ClientProxy
from client.serializers import ClientSerializer
from core.api.permissions import BaseApiPermissionMixin
from core.utils import get_formatted_logger

logger = get_formatted_logger()


class ClientViewSet(ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = (permissions.IsAuthenticated, BaseApiPermissionMixin)
    # parser_classes = [parsers.FormParser, parsers.MultiPartParser]
    perm_slug = "client.client"
    queryset = ClientProxy.objects.all()
