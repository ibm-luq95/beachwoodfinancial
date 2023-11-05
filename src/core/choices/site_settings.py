# -*- coding: utf-8 -*-#
import stringcase
from django.db import models
from django.utils.translation import gettext as _

from core.constants.site_settings import (
    SEC_DESC_CLIENT,
    SEC_DESC_TASK,
    SEC_DESC_JOB,
    SEC_DESC_BOOKKEEPER,
    SEC_DESC_NOTE,
    SEC_DESC_CLIENT_CATEGORY,
    SEC_DESC_ASSISTANT,
    SEC_DESC_MANAGER,
    SEC_DESC_DISCUSSION,
    SEC_DESC_REPORT,
    SEC_DESC_CLIENT_ACCOUNT,
    SEC_DESC_SITE_SETTINGS,
    SEC_DESC_APPLICATION_CONFIGURATIONS,
    SEC_DESC_IMPORTANT_CONTACT,
    SEC_DESC_SPECIAL_ASSIGNMENT,
    SEC_DESC_JOB_CATEGORY,
    SEC_DESC_DOCUMENT,
    SEC_DESC_REQUESTED_ASSIGNMENT,
)


class SectionDescriptionEnum(models.TextChoices):
    CLIENT = SEC_DESC_CLIENT, _(stringcase.sentencecase(SEC_DESC_CLIENT))
    JOB = SEC_DESC_JOB, _(stringcase.sentencecase(SEC_DESC_JOB))
    TASK = SEC_DESC_TASK, _(stringcase.sentencecase(SEC_DESC_TASK))
    SPECIAL_ASSIGNMENT = SEC_DESC_SPECIAL_ASSIGNMENT, _(
        stringcase.sentencecase(SEC_DESC_SPECIAL_ASSIGNMENT)
    )
    REQUESTED_ASSIGNMENT = SEC_DESC_REQUESTED_ASSIGNMENT, _(
        stringcase.sentencecase(SEC_DESC_REQUESTED_ASSIGNMENT)
    )
    CLIENT_ACCOUNT = SEC_DESC_CLIENT_ACCOUNT, _(
        stringcase.sentencecase(SEC_DESC_CLIENT_ACCOUNT)
    )
    JOB_CATEGORY = SEC_DESC_JOB_CATEGORY, _(stringcase.sentencecase(SEC_DESC_JOB_CATEGORY))
    BOOKKEEPER = SEC_DESC_BOOKKEEPER, _(stringcase.sentencecase(SEC_DESC_BOOKKEEPER))
    DOCUMENT = SEC_DESC_DOCUMENT, _(stringcase.sentencecase(SEC_DESC_DOCUMENT))
    NOTE = SEC_DESC_NOTE, _(stringcase.sentencecase(SEC_DESC_NOTE))
    CLIENT_CATEGORY = SEC_DESC_CLIENT_CATEGORY, _(
        stringcase.sentencecase(SEC_DESC_CLIENT_CATEGORY)
    )
    ASSISTANT = SEC_DESC_ASSISTANT, _(stringcase.sentencecase(SEC_DESC_ASSISTANT))
    MANAGER = SEC_DESC_MANAGER, _(stringcase.sentencecase(SEC_DESC_MANAGER))
    DISCUSSION = SEC_DESC_DISCUSSION, _(stringcase.sentencecase(SEC_DESC_DISCUSSION))
    REPORT = SEC_DESC_REPORT, _(stringcase.sentencecase(SEC_DESC_REPORT))
    SITE_SETTINGS = SEC_DESC_SITE_SETTINGS, _(
        stringcase.sentencecase(SEC_DESC_SITE_SETTINGS)
    )
    APPLICATION_CONFIGURATIONS = SEC_DESC_APPLICATION_CONFIGURATIONS, _(
        stringcase.sentencecase(SEC_DESC_APPLICATION_CONFIGURATIONS)
    )
    IMPORTANT_CONTACT = SEC_DESC_IMPORTANT_CONTACT, _(
        stringcase.sentencecase(SEC_DESC_IMPORTANT_CONTACT)
    )
