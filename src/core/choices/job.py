# -*- coding: utf-8 -*-#
import stringcase
from django.db import models
from django.utils.translation import gettext as _

from core.constants.status_labels import (
    CON_NOT_STARTED,
    CON_ARCHIVED,
    CON_IN_PROGRESS,
    CON_PAST_DUE,
    CON_COMPLETED,
    CON_NOT_COMPLETED,
    CON_DRAFT,
    CON_NEED_INFO,
    CON_STALLED,
    CON_ONGOING,
)
from core.constants.types_labels import (
    CON_NO_TYPE,
    CON_RECURRING,
    CON_URGENT,
    CON_WEEKLY,
    CON_YEARLY,
    CON_MONTHLY,
    CON_QUARTERLY,
    CON_ONE_TIME,
)


class JobTypeEnum(models.TextChoices):
    NO_TYPE = CON_NO_TYPE, _(stringcase.sentencecase(CON_NO_TYPE))
    RECURRING = CON_RECURRING, _(stringcase.sentencecase(CON_RECURRING))
    WEEKLY = CON_WEEKLY, _(stringcase.sentencecase(CON_WEEKLY))
    MONTHLY = CON_MONTHLY, _(stringcase.sentencecase(CON_MONTHLY))
    QUARTERLY = CON_QUARTERLY, _(stringcase.sentencecase(CON_QUARTERLY))
    YEARLY = CON_YEARLY, _(stringcase.sentencecase(CON_YEARLY))
    ONE_TIME = CON_ONE_TIME, _(stringcase.sentencecase(CON_ONE_TIME))
    URGENT = CON_URGENT, _(stringcase.sentencecase(CON_URGENT))


class JobStatusEnum(models.TextChoices):
    NOT_STARTED = CON_NOT_STARTED, _(stringcase.sentencecase(CON_NOT_STARTED))
    IN_PROGRESS = CON_IN_PROGRESS, _(stringcase.sentencecase(CON_IN_PROGRESS))
    PAST_DUE = CON_PAST_DUE, _(stringcase.sentencecase(CON_PAST_DUE))
    COMPLETED = CON_COMPLETED, _(stringcase.sentencecase(CON_COMPLETED))
    NOT_COMPLETED = CON_NOT_COMPLETED, _(stringcase.sentencecase(CON_NOT_COMPLETED))
    ARCHIVED = CON_ARCHIVED, _(stringcase.sentencecase(CON_ARCHIVED))
    DRAFT = CON_DRAFT, _(stringcase.sentencecase(CON_DRAFT))


class JobStateEnum(models.TextChoices):
    NEED_INFO = CON_NEED_INFO, _(stringcase.sentencecase(CON_NEED_INFO))
    STALLED = CON_STALLED, _(stringcase.sentencecase(CON_STALLED))
    ONGOING = CON_ONGOING, _(stringcase.sentencecase(CON_ONGOING))
