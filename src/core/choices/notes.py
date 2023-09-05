# -*- coding: utf-8 -*-#
import stringcase
from django.db import models
from django.utils.translation import gettext as _

from core.constants.general import CON_TASK, CON_CLIENT, CON_JOB
from core.constants.status_labels import CON_ENABLED, CON_DISABLED, CON_ARCHIVED


class NoteSectionEnum(models.TextChoices):
    CLIENT = CON_CLIENT, _(stringcase.sentencecase(CON_CLIENT))
    JOB = CON_JOB, _(stringcase.sentencecase(CON_JOB))
    TASK = CON_TASK, _(stringcase.sentencecase(CON_TASK))


class NoteStatusEnum(models.TextChoices):
    ENABLED = CON_ENABLED, _(stringcase.sentencecase(CON_ENABLED))
    DISABLED = CON_DISABLED, _(stringcase.sentencecase(CON_DISABLED))
    ARCHIVE = CON_ARCHIVED, _(stringcase.sentencecase(CON_ARCHIVED))
