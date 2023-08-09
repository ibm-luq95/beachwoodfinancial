# -*- coding: utf-8 -*-#
from rest_framework import serializers

from special_assignment.models import SpecialAssignmentProxy


class SpecialAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialAssignmentProxy
        exclude = ("metadata", "is_deleted")
        # depth = 1
