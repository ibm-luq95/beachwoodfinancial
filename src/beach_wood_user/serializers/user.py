# -*- coding: utf-8 -*-#
from rest_framework import serializers

from beach_wood_user.models import BWUser
from core.constants import EXCLUDED_FIELDS


class BeachWoodUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BWUser
        exclude = EXCLUDED_FIELDS + ["password", "created_at"]
        depth = 1
