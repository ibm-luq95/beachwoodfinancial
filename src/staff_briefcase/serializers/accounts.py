# -*- coding: utf-8 -*-#
import traceback

from django.db import transaction
from rest_framework import serializers

from staff_briefcase.models import StaffAccounts, StaffBriefcase


class StaffAccountsSerializer(serializers.ModelSerializer):
    briefcase = serializers.UUIDField(required=True)

    class Meta:
        model = StaffAccounts
        fields = ("title", "url", "briefcase", "username_email", "password", "name")
        depth = 1

    def create(self, validated_data):
        try:
            with transaction.atomic():
                briefcase_pk = validated_data.pop("briefcase")
                briefcase_obj = StaffBriefcase.objects.get(pk=briefcase_pk)
                obj = StaffAccounts.objects.create(**validated_data)
                # BWDebuggingPrint.pprint(obj.password)
                briefcase_obj.accounts.add(obj)
                briefcase_obj.save()
                # obj.save(foo=validated_data["foo"])
                return obj
        except Exception as ex:
            print(traceback.format_exc())
