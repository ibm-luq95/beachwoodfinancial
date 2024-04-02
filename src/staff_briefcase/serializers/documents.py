# -*- coding: utf-8 -*-#
import traceback

from django.db import transaction
from rest_framework import serializers

from staff_briefcase.models import StaffBriefcase, StaffDocuments


class StaffDocumentsSerializer(serializers.ModelSerializer):
    briefcase = serializers.UUIDField(required=True)

    class Meta:
        model = StaffDocuments
        fields = ("title", "document_file", "briefcase")
        # exclude = EXCLUDED_FIELDS
        depth = 1

    def create(self, validated_data):
        try:
            with transaction.atomic():
                briefcase_pk = validated_data.pop("briefcase")
                briefcase_obj = StaffBriefcase.objects.get(pk=briefcase_pk)
                obj = StaffDocuments.objects.create(**validated_data)
                briefcase_obj.documents.add(obj)
                briefcase_obj.save()
                # obj.save(foo=validated_data["foo"])
                return obj
        except Exception as ex:
            print(traceback.format_exc())
