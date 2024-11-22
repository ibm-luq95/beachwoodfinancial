# -*- coding: utf-8 -*-#
from django.utils import timezone
from django.utils.translation import gettext as _
from rest_framework import serializers


class ValidateDueDateSerializerMixin:
    """
    Mixin class that validates the due date and start date of a serializer.

    This mixin class adds a validation method to a serializer that checks if the due date is in the past and if the start date is after the due date. It raises a `ValidationError` if either condition is not met.

    Args:
        self: The object instance.
        data (dict): The data to be validated.

    Returns:
        dict: The validated data.

    Raises:
        serializers.ValidationError: If the due date is in the past or if the start date is after the due date.

    """

    def validate(self, data):
        """
        Validates the due date and start date of the serializer.

        This method checks if the due date is in the past and if the start date is after the due date.
        It raises a `ValidationError` if either condition is not met.

        Args:
            self: The object instance.
            data (dict): The data to be validated.

        Returns:
            dict: The validated data.

        Raises:
            serializers.ValidationError: If the due date is in the past or if the start date is after the due date.
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
