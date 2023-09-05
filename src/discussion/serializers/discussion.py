# -*- coding: utf-8 -*-#
from rest_framework import serializers

from discussion.models import DiscussionProxy
from job.models import JobProxy
from special_assignment.models import SpecialAssignment


class DiscussionSerializer(serializers.ModelSerializer):
    special_assignment = serializers.PrimaryKeyRelatedField(
        queryset=SpecialAssignment.objects.all(), many=False, required=False
    )
    replies = serializers.PrimaryKeyRelatedField(
        queryset=DiscussionProxy.objects.all(), many=False, required=False
    )
    job = serializers.PrimaryKeyRelatedField(
        queryset=JobProxy.objects.all(), many=False, required=False
    )
    replies = serializers.PrimaryKeyRelatedField(
        queryset=DiscussionProxy.objects.all(), many=False, required=False
    )

    class Meta:
        model = DiscussionProxy
        exclude = ("metadata", "is_deleted")
        # depth = 1
