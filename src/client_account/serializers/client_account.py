# -*- coding: utf-8 -*-#
from rest_framework import serializers

from client_account.models import ClientAccount
from core.constants import EXCLUDED_FIELDS


class ClientAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientAccount
        exclude = EXCLUDED_FIELDS
        # depth = 1
