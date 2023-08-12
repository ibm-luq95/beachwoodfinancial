# -*- coding: utf-8 -*-#
from rest_framework import serializers
from note.models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        exclude = (
            "metadata",
            "is_deleted",
            # "created_at",
            "updated_at",
            "deleted_at",
        )
        # depth = 1
