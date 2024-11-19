# -*- coding: utf-8 -*-#
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

from django.utils.dateparse import parse_date


class ValidateDueDateMixin:
    """
    A mixin class that validates the due date of a model.

    This mixin class adds a validation method to a model that checks if the due date is in the past.
    It raises a ValidationError if the due date is in the past.

    Methods:
        clean(self) -> None: Validates the due date of the model.

    """

    def clean(self):
        """
        Validates the due date of the model.

        This method checks if the due date is in the past and raises a ValidationError if it is.
        It also calls the clean method of the parent class.

        Raises:
            ValidationError: If the due date is in the past.

        Returns:
            None

        """
        if hasattr(self, "due_date"):
            now = timezone.now().date()
            if isinstance(self.due_date, str):
                due_date = parse_date(self.due_date)
            else:
                due_date = self.due_date
            if self.get_changed_columns().get("due_date") != due_date:
                if due_date < timezone.now().date():
                    raise ValidationError(
                        {"due_date": _("The date cannot be in the past!")}
                    )
        super(ValidateDueDateMixin, self).clean()
