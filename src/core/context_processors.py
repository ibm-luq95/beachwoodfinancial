# -*- coding: utf-8 -*-#
from core.constants.general import (
    DEFAULT_FULL_DATE_TIME_FORMAT,
    DEFAULT_TEMPLATE_TABLE_LIST_TRUNCATED_STRING,
    DEFAULT_TEMPLATE_TABLE_LIST_LONG_TRUNCATED_STRING,
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
    NEED_INFO,
    STALLED,
    ONGOING,
)


def access_css_classes_constants(request) -> dict:
    return {
        "BW_TAILWIDCSS_TEXT_INPUT_CSS_CLASSES": (
            "py-2 px-3 pr-11 block w-full border-gray-200 shadow-sm text-sm rounded-lg "
            "focus:border-blue-500 focus:ring-blue-500 dark:bg-slate-900 "
            "dark:border-gray-700 dark:text-gray-400"
        )
    }


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
        "NEED_INFO": NEED_INFO,
        "STALLED": STALLED,
        "ONGOING": ONGOING,
        "DEFAULT_TEMPLATE_TABLE_LIST_TRUNCATED_STRING": DEFAULT_TEMPLATE_TABLE_LIST_TRUNCATED_STRING,
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
            "NEED_INFO": NEED_INFO,
            "STALLED": STALLED,
            "ONGOING": ONGOING,
            "DEFAULT_TEMPLATE_TABLE_LIST_TRUNCATED_STRING": DEFAULT_TEMPLATE_TABLE_LIST_TRUNCATED_STRING,
            "DEFAULT_TEMPLATE_TABLE_LIST_LONG_TRUNCATED_STRING": DEFAULT_TEMPLATE_TABLE_LIST_LONG_TRUNCATED_STRING,
        }
    }
