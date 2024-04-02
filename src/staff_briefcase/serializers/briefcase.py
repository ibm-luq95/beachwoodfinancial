# -*- coding: utf-8 -*-#
from rest_framework import serializers

from beach_wood_user.serializers import BWUserSerializer
from staff_briefcase.models import StaffBriefcase


class StaffBriefcaseSerializer(serializers.ModelSerializer):
    user = BWUserSerializer(read_only=True)

    class Meta:
        model = StaffBriefcase
        exclude = (
            "metadata",
            "is_deleted",
            # "created_at",
            "updated_at",
            "deleted_at",
        )
        # depth = 1
