# -*- coding: utf-8 -*-#
from django.contrib import admin

from note.models import Note
from core.admin import BWBaseAdminModelMixin


@admin.register(Note)
class NoteAdmin(BWBaseAdminModelMixin):
    pass
