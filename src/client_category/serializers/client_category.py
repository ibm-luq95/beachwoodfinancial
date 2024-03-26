# -*- coding: utf-8 -*-#
from rest_framework import serializers

from client_category.models import ClientCategory


class ClientCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientCategory
        fields = ["name"]
