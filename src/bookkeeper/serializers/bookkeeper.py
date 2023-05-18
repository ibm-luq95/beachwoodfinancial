# -*- coding: utf-8 -*-#
from rest_framework import serializers

from beach_wood_user.serializers import BWUserSerializer
from bookkeeper.models import BookkeeperProxy
from core.constants import EXCLUDED_FIELDS


class BookkeeperSerializer(serializers.ModelSerializer):
    user = BWUserSerializer(read_only=True)

    class Meta:
        model = BookkeeperProxy
        exclude = EXCLUDED_FIELDS
        depth = 1
