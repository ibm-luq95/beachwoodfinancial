# -*- coding: utf-8 -*-#
from rest_framework import serializers

from beach_wood_user.models import BWUser
from discussion.models import DiscussionProxy
from job.models import JobProxy
from special_assignment.models import SpecialAssignmentProxy


class DiscussionSerializer(serializers.ModelSerializer):
    special_assignment = serializers.PrimaryKeyRelatedField(
        queryset=SpecialAssignmentProxy.objects.all(), many=False, required=False
    )
    replies = serializers.PrimaryKeyRelatedField(
        queryset=DiscussionProxy.objects.all(), many=False, required=False
    )
    job = serializers.PrimaryKeyRelatedField(
        queryset=JobProxy.objects.all(), many=False, required=False
    )
    sender = serializers.PrimaryKeyRelatedField(
        queryset=BWUser.objects.all(), many=False, required=False
    )

    class Meta:
        model = DiscussionProxy
        exclude = ("metadata", "is_deleted")
        # depth = 1
