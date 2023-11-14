# -*- coding: utf-8 -*-#
import stringcase
from django.db import models
from django.utils.translation import gettext as _

from core.constants.status_labels import (
    CON_NOT_STARTED,
    CON_COMPLETED,
    CON_IN_PROGRESS,
    CON_ARCHIVED,
    CON_REJECTED,
    CON_PAST_DUE,
)


class SpecialAssignmentStatusEnum(models.TextChoices):
    NOT_STARTED = CON_NOT_STARTED, _(stringcase.sentencecase(CON_NOT_STARTED))
    IN_PROGRESS = CON_IN_PROGRESS, _(stringcase.sentencecase(CON_IN_PROGRESS))
    PAST_DUE = CON_PAST_DUE, _(stringcase.sentencecase(CON_PAST_DUE))
    COMPLETED = CON_COMPLETED, _(stringcase.sentencecase(CON_COMPLETED))
    REJECTED = CON_REJECTED, _(stringcase.sentencecase(CON_REJECTED))
    ARCHIVED = CON_ARCHIVED, _(stringcase.sentencecase(CON_ARCHIVED))
