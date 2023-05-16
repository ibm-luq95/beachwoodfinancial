# -*- coding: utf-8 -*-#
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _


class DueDateOnlyMixin(models.Model):
    due_date = models.DateField(_("due date"), default=timezone.now, null=True, blank=True)

    class Meta:
        abstract = True
