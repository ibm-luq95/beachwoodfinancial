# -*- coding: utf-8 -*-#
from rest_framework import serializers

from core.constants import EXCLUDED_FIELDS
from document.models import Document


class DocumentSerializer(serializers.ModelSerializer):
    # document_file = serializers.FileField(use_url=True, allow_empty_file=False)
    # job = serializers.PrimaryKeyRelatedField(
    #     queryset=Job.objects.all(), many=False, required=False
    # )

    class Meta:
        model = Document
        exclude = EXCLUDED_FIELDS
        # depth = 1
