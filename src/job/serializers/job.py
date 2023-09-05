from django.utils import timezone
from rest_framework import serializers

from beach_wood_user.models import BWUser
from client.models import ClientProxy
from core.constants import EXCLUDED_FIELDS
from job.models import JobProxy
from job_category.models import JobCategory
from task.serializers import TaskSerializer


class JobSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True, required=False)
    client = serializers.PrimaryKeyRelatedField(
        queryset=ClientProxy.objects.all(), many=False
    )
    managed_by = serializers.PrimaryKeyRelatedField(
        queryset=BWUser.objects.all(), many=False, allow_null=True
    )
    # categories = JobCategorySerializer(read_only=True, many=True)
    categories = serializers.PrimaryKeyRelatedField(
        queryset=JobCategory.objects.all(), many=True, required=False
    )

    # due_date = serializers.DateField(read_only=True)

    # bookkeeper = BookkeeperSerializer(many=True, read_only=True)
    # assistants = AssistantSerializer(many=True, read_only=True)

    class Meta:
        model = JobProxy
        exclude = EXCLUDED_FIELDS
        depth = 2

    def validate(self, data):
        """
        Check that start is before finish.
        """
        now = timezone.now().date()
        if self.context.get("request").method != "PUT":
            if data["due_date"] < now:
                raise serializers.ValidationError({"due_date": "Due date old!"})
        return data

    def update(self, instance, validated_data):
        categories = validated_data.get("categories")
        if categories:
            instance.categories.clear()
            for category in categories:
                instance.categories.add(category)
        instance = super().update(instance, validated_data)
        return instance
