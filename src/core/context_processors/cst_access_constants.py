# -*- coding: utf-8 -*-#
from core.constants.css_classes import BW_INFO_MODAL_CSS_CLASSES
from core.constants.general import (
    DEFAULT_FULL_DATE_TIME_FORMAT,
    DEFAULT_TEMPLATE_TABLE_LIST_TRUNCATED_STRING,
    DEFAULT_TEMPLATE_TABLE_LIST_TRUNCATED_STRING_WIDGETS,
    DEFAULT_TEMPLATE_TABLE_LIST_LONG_TRUNCATED_STRING,
    IS_SHOW_CREATED_AT,
    DEFAULT_MEDIUM_TRUNCATED_STRING,
    DEFAULT_LONG_TRUNCATED_STRING,
    DEFAULT_SHORT_TRUNCATED_STRING,
)
from core.constants.status_labels import (
    CON_ENABLED,
    CON_COMPLETED,
    CON_ARCHIVED,
    CON_IN_PROGRESS,
    CON_DISABLED,
    CON_REJECTED,
    CON_NOT_STARTED,
    CON_NOT_COMPLETED,
    CON_PAST_DUE,
    CON_DRAFT,
    CON_PENDING,
    CON_CANCELED,
    CON_NEED_INFO,
    CON_STALLED,
    CON_ONGOING,
)
from core.constants.users import (
    CON_BOOKKEEPER,
    CON_ASSISTANT,
    CON_MANAGER,
    CON_DEVELOPER,
    CON_USER,
)


def access_constants(request) -> dict:
    """
    The context processor will return project constants as dict
    """
    return {
        "CON_ENABLED": CON_ENABLED,
        "CON_IN_PROGRESS": CON_IN_PROGRESS,
        "CON_ARCHIVED": CON_ARCHIVED,
        "CON_COMPLETED": CON_COMPLETED,
        "CON_DISABLED": CON_DISABLED,
        "CON_REJECTED": CON_REJECTED,
        "CON_NOT_STARTED": CON_NOT_STARTED,
        "CON_NOT_COMPLETED": CON_NOT_COMPLETED,
        "CON_PAST_DUE": CON_PAST_DUE,
        "CON_PENDING": CON_PENDING,
        "CON_CANCELED": CON_CANCELED,
        "CON_DRAFT": CON_DRAFT,
        "DEFAULT_FULL_DATE_TIME_FORMAT": DEFAULT_FULL_DATE_TIME_FORMAT,
        "CON_NEED_INFO": CON_NEED_INFO,
        "CON_STALLED": CON_STALLED,
        "CON_ONGOING": CON_ONGOING,
        "IS_SHOW_CREATED_AT": IS_SHOW_CREATED_AT,
        "CON_BOOKKEEPER": CON_BOOKKEEPER,
        "CON_ASSISTANT": CON_ASSISTANT,
        "CON_MANAGER": CON_MANAGER,
        "CON_DEVELOPER": CON_DEVELOPER,
        "CON_USER": CON_USER,
        "BW_INFO_MODAL_CSS_CLASSES": BW_INFO_MODAL_CSS_CLASSES,
        "DEFAULT_TEMPLATE_TABLE_LIST_TRUNCATED_STRING": (
            DEFAULT_TEMPLATE_TABLE_LIST_TRUNCATED_STRING
        ),
        "DEFAULT_TEMPLATE_TABLE_LIST_TRUNCATED_STRING_WIDGETS": (
            DEFAULT_TEMPLATE_TABLE_LIST_TRUNCATED_STRING_WIDGETS
        ),
        "DEFAULT_SHORT_TRUNCATED_STRING": DEFAULT_SHORT_TRUNCATED_STRING,
    }


def access_constants_as_group(request) -> dict:
    """
    The context processor will return project constants as dict
    """
    return {
        "ALL_CONS": {
            "CON_ENABLED": CON_ENABLED,
            "CON_IN_PROGRESS": CON_IN_PROGRESS,
            "CON_ARCHIVED": CON_ARCHIVED,
            "CON_COMPLETED": CON_COMPLETED,
            "CON_DISABLED": CON_DISABLED,
            "CON_REJECTED": CON_REJECTED,
            "CON_NOT_STARTED": CON_NOT_STARTED,
            "CON_NOT_COMPLETED": CON_NOT_COMPLETED,
            "CON_PAST_DUE": CON_PAST_DUE,
            "CON_PENDING": CON_PENDING,
            "CON_CANCELED": CON_CANCELED,
            "CON_DRAFT": CON_DRAFT,
            "DEFAULT_FULL_DATE_TIME_FORMAT": DEFAULT_FULL_DATE_TIME_FORMAT,
            "CON_NEED_INFO": CON_NEED_INFO,
            "CON_STALLED": CON_STALLED,
            "CON_ONGOING": CON_ONGOING,
            "DEFAULT_TEMPLATE_TABLE_LIST_TRUNCATED_STRING": (
                DEFAULT_TEMPLATE_TABLE_LIST_TRUNCATED_STRING
            ),
            "DEFAULT_LONG_TRUNCATED_STRING": DEFAULT_LONG_TRUNCATED_STRING,
            "DEFAULT_MEDIUM_TRUNCATED_STRING": DEFAULT_MEDIUM_TRUNCATED_STRING,
            "DEFAULT_TEMPLATE_TABLE_LIST_LONG_TRUNCATED_STRING": (
                DEFAULT_TEMPLATE_TABLE_LIST_LONG_TRUNCATED_STRING
            ),
        }
    }
