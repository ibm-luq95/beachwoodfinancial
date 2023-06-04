# -*- coding: utf-8 -*-#
from core.constants.css_classes import (
    BW_PRELINE_TEXT_INPUT_CSS_CLASSES,
    BW_PRELINE_BASE_TABLE,
    BW_BASE_INPUT_CSS_CLASSES,
    BW_DISABLED_ANCHOR_CSS_CLASSES,
    BW_DISABLED_DISABLED_INPUTS_CSS_CLASSES,
    BW_TABLE_LIST_COMPONENT_CLASS,
    BW_FULL_INPUT_CSS_CLASSES,
    BW_PRELINE_BASE_BUTTON,
    BW_PRELINE_INPUT_DANGER_STATE,
    BW_PRELINE_INPUT_SUCCESS_STATE,
    BW_TABLE_LIST_SORT_CLASS,
    BW_TABLE_CONTAINER,
    BW_PRELINE_FILTER_TEXT_INPUT,
    BW_PRELINE_FILTER_SELECT_INPUT_DEFAULT,
)


def access_css_classes_constants(request) -> dict:
    return {
        "BW_PRELINE_TEXT_INPUT_CSS_CLASSES": BW_PRELINE_TEXT_INPUT_CSS_CLASSES,
        "BW_PRELINE_BASE_TABLE": BW_PRELINE_BASE_TABLE,
        "BW_TABLE_LIST_SORT_CLASS": BW_TABLE_LIST_SORT_CLASS,
        "BW_PRELINE_FILTER_SELECT_INPUT_DEFAULT": BW_PRELINE_FILTER_SELECT_INPUT_DEFAULT,
        "BW_TABLE_CONTAINER": BW_TABLE_CONTAINER,
        "BW_BASE_INPUT_CSS_CLASSES": BW_BASE_INPUT_CSS_CLASSES,
        "BW_PRELINE_FILTER_TEXT_INPUT": BW_PRELINE_FILTER_TEXT_INPUT,
        "BW_PRELINE_INPUT_DANGER_STATE": BW_PRELINE_INPUT_DANGER_STATE,
        "BW_PRELINE_INPUT_SUCCESS_STATE": BW_PRELINE_INPUT_SUCCESS_STATE,
        "BW_DISABLED_ANCHOR_CSS_CLASSES": BW_DISABLED_ANCHOR_CSS_CLASSES,
        "BW_DISABLED_DISABLED_INPUTS_CSS_CLASSES": BW_DISABLED_DISABLED_INPUTS_CSS_CLASSES,
        "BW_TABLE_LIST_COMPONENT_CLASS": BW_TABLE_LIST_COMPONENT_CLASS,
        "BW_FULL_INPUT_CSS_CLASSES": BW_FULL_INPUT_CSS_CLASSES,
        "BW_DEFAULT_BUTTONS_CSS_CLASSES": {
            "SMALL": f"py-2 px-3 {BW_PRELINE_BASE_BUTTON}",
            "DEFAULT": f"py-3 px-4 {BW_PRELINE_BASE_BUTTON}",
            "LARGE": f"py-3 px-4 {BW_PRELINE_BASE_BUTTON}",
        },
        "SOLID_COLORS_CSS_CLASSES": {
            "DARK": (
                "bg-gray-800 text-white hover:bg-gray-900 focus:outline-none focus:ring-2 focus:ring-gray-800 "
                "focus:ring-offset-2 dark:focus:ring-gray-900 dark:focus:ring-offset-gray-800"
            ),
            "GRAY": (
                "bg-gray-500 text-white hover:bg-gray-600 focus:outline-none focus:ring-2 focus:ring-gray-500 "
                "focus:ring-offset-2 dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-offset-gray-800"
            ),
            "DANGER": (
                "bg-red-500 text-white hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-red-500 "
                "focus:ring-offset-2 dark:focus:ring-offset-gray-800"
            ),
            "WARNING": (
                "bg-yellow-500 text-white hover:bg-yellow-600 focus:outline-none focus:ring-2 focus:ring-yellow-500 "
                "focus:ring-offset-2 dark:focus:ring-offset-gray-800"
            ),
            "SUCCESS": (
                "bg-green-500 text-white hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-green-500 "
                "focus:ring-offset-2 dark:focus:ring-offset-gray-800"
            ),
            "PRIMARY": (
                "bg-blue-500 text-white hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 "
                "focus:ring-offset-2 dark:focus:ring-offset-gray-800"
            ),
            "INFO": (
                "bg-indigo-500 text-white hover:bg-indigo-600 focus:outline-none focus:ring-2 focus:ring-indigo-500 "
                "focus:ring-offset-2 dark:focus:ring-offset-gray-800"
            ),
            "LIGHT": (
                "bg-white text-gray-600 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-white "
                "focus:ring-offset-2 dark:focus:ring-offset-gray-800"
            ),
            "PINK": (
                "bg-pink-500 text-white hover:bg-pink-600 focus:outline-none focus:ring-2 focus:ring-pink-500 "
                "focus:ring-offset-2 dark:focus:ring-offset-gray-800"
            ),
            "PURPLE": (
                "bg-purple-500 text-white hover:bg-purple-600 focus:outline-none focus:ring-2 focus:ring-purple-500 "
                "focus:ring-offset-2 dark:focus:ring-offset-gray-800"
            ),
        },
        "SOFT_COLORS_CSS_CLASSES": {
            "DARK": (
                "bg-gray-100 text-gray-800 hover:text-white hover:bg-gray-800 focus:outline-none focus:ring-2 "
                "ring-offset-white focus:ring-gray-800 focus:ring-offset-2 transition-all text-sm dark:bg-gray-700 "
                "dark:hover:bg-gray-900 dark:text-white"
            ),
            "GRAY": (
                "bg-gray-100 text-gray-500 hover:text-white hover:bg-gray-500 focus:outline-none focus:ring-2 "
                "ring-offset-white focus:ring-gray-500 focus:ring-offset-2 transition-all text-sm dark:bg-gray-700 "
                "dark:hover:bg-gray-600 dark:focus:ring-gray-600 dark:text-white dark:focus:ring-offset-gray-800"
            ),
            "DANGER": (
                "bg-red-100 text-red-500 hover:text-white hover:bg-red-300 focus:outline-none focus:ring-2 "
                "ring-offset-white focus:ring-red-500 focus:ring-offset-2 transition-all text-sm "
                "dark:focus:ring-offset-gray-800"
            ),
            "WARNING": (
                "bg-yellow-100 text-yellow-500 hover:text-white hover:bg-yellow-100 focus:outline-none focus:ring-2 "
                "ring-offset-white focus:ring-yellow-500 focus:ring-offset-2 transition-all text-sm "
                "dark:focus:ring-offset-gray-800"
            ),
            "SUCCESS": (
                "bg-green-100 text-green-500 hover:text-white hover:bg-green-100 focus:outline-none focus:ring-2 "
                "ring-offset-white focus:ring-green-500 focus:ring-offset-2 transition-all text-sm "
                "dark:focus:ring-offset-gray-800"
            ),
            "PRIMARY": (
                "bg-blue-100 text-blue-500 hover:text-white hover:bg-blue-100 focus:outline-none focus:ring-2 "
                "ring-offset-white focus:ring-blue-500 focus:ring-offset-2 transition-all text-sm "
                "dark:focus:ring-offset-gray-800"
            ),
            "INFO": (
                "bg-indigo-100 text-indigo-500 hover:text-white hover:bg-indigo-100 focus:outline-none focus:ring-2 "
                "ring-offset-white focus:ring-indigo-500 focus:ring-offset-2 transition-all text-sm "
                "dark:focus:ring-offset-gray-800"
            ),
            "LIGHT": (
                "bg-white text-gray-100 hover:text-gray-600 hover:bg-white focus:outline-none focus:ring-2 "
                "ring-offset-white focus:ring-white focus:ring-offset-2 transition-all text-sm "
                "dark:focus:ring-offset-gray-800"
            ),
            "PINK": (
                "bg-pink-100 text-pink-500 hover:text-white hover:bg-pink-100 focus:outline-none focus:ring-2 "
                "ring-offset-white focus:ring-pink-500 focus:ring-offset-2 transition-all text-sm "
                "dark:focus:ring-offset-gray-800"
            ),
            "PURPLE": (
                "bg-purple-100 text-purple-500 hover:text-white hover:bg-purple-100 focus:outline-none focus:ring-2 "
                "ring-offset-white focus:ring-purple-500 focus:ring-offset-2 transition-all text-sm "
                "dark:focus:ring-offset-gray-800"
            ),
        },
        "BUTTONS_CSS_CLASSES": {
            "SOLID": (
                "py-3 px-4 inline-flex justify-center items-center gap-2 rounded-md border border-transparent "
                "font-semibold transition-all text-sm"
            ),
            "SOFT": (
                "py-3 px-4 inline-flex justify-center items-center gap-2 rounded-md border transition-all text-sm "
                "border-transparent font-semibold"
            ),
            "OUTLINE": (
                "py-[.688rem] px-4 inline-flex justify-center items-center gap-2 rounded-md border-2 font-semibold "
                "transition-all text-sm"
            ),
            "LINK": (
                "py-3 px-4 inline-flex justify-center items-center gap-2 rounded-md border border-transparent "
                "font-semibold transition-all text-sm"
            ),
            "WHITE": (
                "py-3 px-4 inline-flex justify-center items-center gap-2 rounded-md border font-medium transition-all "
                "text-sm shadow-sm align-middle"
            ),
            "GHOST": (
                "py-3 px-4 inline-flex justify-center items-center gap-2 rounded-md border border-transparent "
                "font-semibold transition-all text-sm"
            ),
        },
    }
