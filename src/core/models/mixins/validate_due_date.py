# -*- coding: utf-8 -*-#
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

from django.utils.dateparse import parse_date


class ValidateDueDateMixin:
    def clean(self):
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
