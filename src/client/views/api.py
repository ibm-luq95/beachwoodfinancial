# -*- coding: utf-8 -*-#
from django.http import HttpRequest
from rest_framework import permissions, parsers, status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import APIException

from bookkeeper.models import BookkeeperProxy
from client.models import ClientProxy
from client.serializers import ClientSerializer
from core.api.permissions import BaseApiPermissionMixin
from core.utils import get_formatted_logger
from core.utils.developments.debugging_print_object import BWDebuggingPrint

logger = get_formatted_logger()


class ClientViewSet(ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = (permissions.IsAuthenticated, BaseApiPermissionMixin)
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]
    perm_slug = "client.client"
    queryset = ClientProxy.objects.all()

    @action(
        methods=["POST"],
        detail=False,
        url_path="assign_bookkeeper",
        parser_classes=[parsers.JSONParser],
    )
    def assign_bookkeeper(self, request: HttpRequest, pk=None, *args, **kwargs):
        try:
            data = {}
            client_pk: str = request.data.get("client")
            bookkeeper_pks: list[str] = request.data.get("bookkeepers")
            if not client_pk:
                raise APIException("Client pk is required!")
            if not bookkeeper_pks:
                raise APIException("Bookkeepers is required!")
            client_obj = ClientProxy.objects.get(pk=client_pk)
            bookkeepers_obj = list(BookkeeperProxy.objects.filter(pk__in=bookkeeper_pks))
            client_obj.bookkeepers.add(*bookkeepers_obj)
            client_obj.save()
            data["client_name"] = client_obj.name
            data["bookkeepers"] = ", ".join([bk.user.fullname for bk in bookkeepers_obj])
            data["success_msg"] = (
                f"Bookkeepers {data['bookkeepers']} assigned to client {data['client_name']} "
                f"successfully"
            )
            return Response(
                data=data, status=status.HTTP_200_OK, content_type="application/json"
            )
        except Exception as ex:
            return Response(
                data={"error": str(ex)},
                status=status.HTTP_400_BAD_REQUEST,
                content_type="application/json",
            )
