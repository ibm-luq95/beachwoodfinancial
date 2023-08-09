# -*- coding: utf-8 -*-#
from django import forms
from django.db import transaction

from core.constants.form import EXCLUDED_FIELDS
from core.forms import BaseModelFormMixin, JoditFormMixin
from core.utils import debugging_print
from special_assignment.models import SpecialAssignmentProxy


class SpecialAssignmentForm(BaseModelFormMixin, JoditFormMixin):
    field_order = [
        "client",
        "title",
        "body",
        "attachment",
        "start_date",
        "due_date",
        "notes",
        "status",
        "assigned_by",
    ]

    def __init__(self, add_jodit_css_class=False, *args, **kwargs):
        super(SpecialAssignmentForm, self).__init__(*args, **kwargs)
        JoditFormMixin.__init__(self, add_jodit_css_class=add_jodit_css_class)
        # self.fields["assigned_by"].initial = assigned_by
        # self.fields["assigned_by"].widget.attrs.update(
        #     {"class": "readonly-select cursor-not-allowed", "readonly": "readonly"}
        # )

    class Meta(BaseModelFormMixin.Meta):
        model = SpecialAssignmentProxy
        exclude = EXCLUDED_FIELDS + ["is_seen"]

    def save(self, commit=True):
        sa = super().save(commit=False)
        with transaction.atomic():
            if commit:
                assigned_by = self.initial.get("assigned_by", None)
                if assigned_by is not None:
                    sa.assigned_by = assigned_by
                sa.save()
                self.save_m2m()
            return sa
