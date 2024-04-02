# -*- coding: utf-8 -*-#

from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from core.api.permissions import BaseApiPermissionMixin
from core.utils import get_formatted_logger
from staff_briefcase.models import StaffAccounts
from staff_briefcase.serializers import StaffAccountsSerializer

logger = get_formatted_logger()


class StaffAccountsViewSet(ModelViewSet):
    serializer_class = StaffAccountsSerializer
    permission_classes = (permissions.IsAuthenticated, BaseApiPermissionMixin)
    perm_slug = "staff_briefcase.staffaccounts"
    queryset = StaffAccounts.objects.all()
