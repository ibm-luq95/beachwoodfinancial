# -*- coding: utf-8 -*-#
from rest_framework import serializers

from client.models import ClientProxy
from core.constants import EXCLUDED_FIELDS
from document.models import Document
from job.models import JobProxy


class DocumentSerializer(serializers.ModelSerializer):

    job = serializers.PrimaryKeyRelatedField(
        queryset=JobProxy.original_objects.all(),
        many=False,
        # read_only=True,
        # allow_null=True,
        # allow_empty=True,
        required=False
    )
    client = serializers.PrimaryKeyRelatedField(
        queryset=ClientProxy.original_objects.all(),
        many=False,
        required=False
    )

    class Meta:
        model = Document
        exclude = EXCLUDED_FIELDS
        # depth = 1
