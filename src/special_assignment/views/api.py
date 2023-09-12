# -*- coding: utf-8 -*-#

from rest_framework import permissions, parsers, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.api.permissions import BaseApiPermissionMixin
from core.utils import get_formatted_logger, debugging_print
from special_assignment.models import SpecialAssignmentProxy
from special_assignment.serializers import SpecialAssignmentSerializer

logger = get_formatted_logger()


class SpecialAssignmentViewSet(ModelViewSet):
    serializer_class = SpecialAssignmentSerializer
    permission_classes = (permissions.IsAuthenticated, BaseApiPermissionMixin)
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]
    perm_slug = "special_assignment.special_assignmentproxy"
    queryset = SpecialAssignmentProxy.objects.all()
