# -*- coding: utf-8 -*-#
from django.utils import timezone
from django.utils.translation import gettext as _
from rest_framework import serializers


class ValidateDueDateSerializerMixin:
    def validate(self, data):
        """
        Check that start is before finish.
        """
        now = timezone.now().date()
        due_date = data.get("due_date")
        start_date = data.get("start_date")
        if self.context.get("request").method != "PATCH":
            if due_date < now:
                raise serializers.ValidationError({"due_date": _("Due date old!")})
            if start_date > due_date:
                raise serializers.ValidationError(
                    {"start_date": _("Start date bigger than due date!")}
                )
        return data
