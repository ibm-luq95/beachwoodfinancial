# -*- coding: utf-8 -*-#
from rest_framework import serializers

from core.constants import EXCLUDED_FIELDS
from assistant.models import AssistantProxy
from beach_wood_user.serializers import BWUserSerializer


class AssistantSerializer(serializers.ModelSerializer):
    user = BWUserSerializer(read_only=True)

    class Meta:
        model = AssistantProxy
        exclude = EXCLUDED_FIELDS
        depth = 1