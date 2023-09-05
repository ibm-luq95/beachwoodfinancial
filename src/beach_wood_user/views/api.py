# -*- coding: utf-8 -*-#
import traceback

from django.contrib.auth.models import Permission
from django.db.transaction import atomic
from rest_framework import permissions
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from beach_wood_user.models import BWUser
from core.api.permissions import ManagerApiPermission
from core.utils import get_formatted_logger, debugging_print

logger = get_formatted_logger()


class UpdateStaffPermissionsApiView(APIView):
    permission_classes = (permissions.IsAuthenticated, ManagerApiPermission)
    http_method_names = ["post"]

    def post(self, request: Request, *args, **kwargs):
        try:
            with atomic():
                data = dict()
                post_data = request.data
                user = BWUser.objects.get(pk=post_data["user"])
                data["user"] = user.pk
                # delete all current permissions
                user.user_permissions.clear()
                user.save()
                post_permissions = post_data.get("permissions")
                permissions_objs = Permission.objects.filter(pk__in=post_permissions)
                permissions_list = [perm for perm in permissions_objs]
                user.user_permissions.add(*permissions_list)
                user.save()
                return Response(status=status.HTTP_200_OK, data=data)
        except Exception as e:
            logger.error(traceback.format_exc())
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data=str(e))
