# -*- coding: utf-8 -*-#
from rest_framework import serializers

from discussion.models import DiscussionProxy
from special_assignment.models import SpecialAssignment


class DiscussionSerializer(serializers.ModelSerializer):
    special_assignment = serializers.PrimaryKeyRelatedField(
        queryset=SpecialAssignment.objects.all(), many=False
    )
    replies = serializers.PrimaryKeyRelatedField(
        queryset=DiscussionProxy.objects.all(), many=False
    )

    class Meta:
        model = DiscussionProxy
        exclude = ("metadata", "is_deleted")
        # depth = 1
