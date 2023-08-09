# -*- coding: utf-8 -*-#
import traceback

from django.utils.translation import gettext as _
from rest_framework import parsers
from rest_framework import permissions
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from core.api.permissions import BaseApiPermissionMixin
from core.utils import get_formatted_logger
from discussion.serializers import DiscussionSerializer

logger = get_formatted_logger()


class CreateDiscussionApiView(APIView):
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]
    # parser_classes = [parsers.MultiPartParser]
    permission_classes = [permissions.IsAuthenticated, BaseApiPermissionMixin]
    perm_slug = "special_assignment.discussion"

    def post(self, request: Request, *args, **kwargs):
        serializer = ""
        try:
            data = request.data
            # debugging_print(data)
            serializer = DiscussionSerializer(data=data)
            # raise APIException("Stop")
            # debugging_print(serializer.is_valid())
            # debugging_print(serializer)
            if serializer.is_valid(raise_exception=True) is False:
                raise APIException(serializer.errors)
            # debugging_print(serializer.validated_data)
            serializer.save()
            return Response(
                {"msg": _("Reply created successfully!")}, status=status.HTTP_201_CREATED
            )
        except APIException as ex:
            # logger.error("API Exception")
            logger.error(traceback.format_exc())
            response_data = {
                "status": status.HTTP_400_BAD_REQUEST,
                # "user_error_msg": ex.detail,
                "user_error_msg": serializer.errors,
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            # debugging_print(ex)
            logger.error(traceback.format_exc())
            response_data = {
                "status": status.HTTP_400_BAD_REQUEST,
                "error": str(ex),
                # "user_error_msg": "Error while create discussion!",
                # "user_error_msg": serializer.errors,
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
