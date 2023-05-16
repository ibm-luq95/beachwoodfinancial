# -*- coding: utf-8 -*-#
import textwrap

from django.db import models

from core.constants.general import DEFAULT_SHORT_TRUNCATED_STRING


class StrModelMixin(models.Model):
    def __str__(self) -> str:
        if hasattr(self, "title"):
            return textwrap.shorten(
                self.title, width=DEFAULT_SHORT_TRUNCATED_STRING, placeholder="..."
            )
            # return self.title
        elif hasattr(self, "body"):
            return textwrap.shorten(
                self.body, width=DEFAULT_SHORT_TRUNCATED_STRING, placeholder="..."
            )
        elif hasattr(self, "name"):
            return textwrap.shorten(
                self.name, width=DEFAULT_SHORT_TRUNCATED_STRING, placeholder="..."
            )

    class Meta:
        abstract = True
