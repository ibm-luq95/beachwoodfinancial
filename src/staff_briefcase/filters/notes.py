# -*- coding: utf-8 -*-#
from core.filters.filter_created_mixin import FilterCreatedMixin
from note.models import Note
from staff_briefcase.models import StaffNotes


class StaffNotesFilter(FilterCreatedMixin):
    class Meta:
        model = StaffNotes
        fields = {
            "title": ["icontains"],
            "note": ["icontains"],
        }
