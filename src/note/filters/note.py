# -*- coding: utf-8 -*-#

from core.filters.filter_help_text import HelpfulFilterSet
from note.models import Note


class NoteFilter(HelpfulFilterSet):
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
