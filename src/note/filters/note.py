# -*- coding: utf-8 -*-#
from core.filters.filter_created_mixin import FilterCreatedMixin
from note.models import Note


class NoteFilter(FilterCreatedMixin):
    class Meta:
        model = Note
        fields = {
            "title": ["icontains"],
            "note_section": ["exact"],
            "client": ["exact"],
            # "job": ["exact"],
            # "task": ["exact"],
            "body": ["icontains"],
        }
