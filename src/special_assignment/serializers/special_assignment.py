# -*- coding: utf-8 -*-#
from rest_framework import serializers

from beach_wood_user.models import BWUser
from job.models import JobProxy
from special_assignment.models import SpecialAssignmentProxy


class SpecialAssignmentSerializer(serializers.ModelSerializer):
    assigned_by = serializers.PrimaryKeyRelatedField(
        default="assigned_by", queryset=BWUser.objects.all()
    )
    job = serializers.PrimaryKeyRelatedField(
        default="job", queryset=JobProxy.objects.all()
    )

    class Meta:
        model = SpecialAssignmentProxy
        exclude = ("metadata", "is_deleted", "deleted_at")
        # fields = ("title", "body", "attachment", "assigned_by")
        # read_only_fields = ("assigned_by",)
        depth = 1
