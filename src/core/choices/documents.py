# -*- coding: utf-8 -*-#
from django.db import models
from django.utils.translation import gettext as _


class DocumentTypesEnum(models.TextChoices):
    CLIENT = "client", _("Client")
    JOB = "job", _("Job")
    TASK = "task", _("Task")
