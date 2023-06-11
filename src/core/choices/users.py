# -*- coding: utf-8 -*-#
import stringcase
from django.db import models
from django.utils.translation import gettext as _

from core.constants.status_labels import (
    CON_ENABLED,
    CON_PENDING,
    CON_CANCELED,
    CON_ARCHIVED,
    CON_DISABLED,
)
from core.constants.users import (
    CON_BOOKKEEPER,
    CON_MANAGER,
    CON_ASSISTANT,
    CON_USER,
    CON_DEVELOPER,
)


class BeachWoodUserTypeEnum(models.TextChoices):
    MANAGER = CON_MANAGER, _(stringcase.sentencecase(CON_MANAGER))
    ASSISTANT = CON_ASSISTANT, _(stringcase.sentencecase(CON_ASSISTANT))
    BOOKKEEPER = CON_BOOKKEEPER, _(stringcase.sentencecase(CON_BOOKKEEPER))


class BeachWoodUserStatusEnum(models.TextChoices):
    ENABLED = CON_ENABLED, _(stringcase.sentencecase(CON_ENABLED))
    PENDING = CON_PENDING, _(stringcase.sentencecase(CON_PENDING))
    CANCELED = CON_CANCELED, _(stringcase.sentencecase(CON_CANCELED))
    DISABLED = CON_DISABLED, _(stringcase.sentencecase(CON_DISABLED))
    ARCHIVED = CON_ARCHIVED, _(stringcase.sentencecase(CON_ARCHIVED))


class BeachWoodUserTypesEnum(models.TextChoices):
    DEVELOPER = CON_DEVELOPER, _(stringcase.sentencecase(CON_DEVELOPER))
    USER = CON_USER, _(stringcase.sentencecase(CON_USER))
