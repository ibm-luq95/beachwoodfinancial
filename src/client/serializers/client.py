# -*- coding: utf-8 -*-#
from rest_framework import serializers
from client.models import ClientProxy


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientProxy
        exclude = ("metadata", "is_deleted")
        # depth = 1
