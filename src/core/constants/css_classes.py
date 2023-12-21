# -*- coding: utf-8 -*-#
from django.utils.translation import gettext as _

from core.constants.identity import BWIdentity

BW_BASE_INPUT_CSS_CLASSES = "bw-input"
BW_DISABLED_ANCHOR_CSS_CLASSES = "bw-disabled-anchor"
BW_DISABLED_DISABLED_INPUTS_CSS_CLASSES = "disabled:opacity-75 cursor-not-allowed"
BW_FULL_INPUT_CSS_CLASSES = (
    f"{BW_BASE_INPUT_CSS_CLASSES} {BW_DISABLED_DISABLED_INPUTS_CSS_CLASSES}"
)
BW_TRAILING_ICON_CSS_CLASSES = (
    f"{BW_FULL_INPUT_CSS_CLASSES} py-2 px-3 pl-11 block w-full border-gray-200 shadow-sm"
    " rounded-md text-sm focus:z-10 focus:border-blue-500 focus:ring-blue-500"
    " dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400"
)
BW_TABLE_LIST_COMPONENT_CLASS = "table-list-component"
BW_TABLE_CONTAINER = "bw-table-container"
BW_TABLE_LIST_SORT_CLASS = "table-sort"
BW_PRELINE_TEXT_INPUT_CSS_CLASSES = (
    f"{BW_BASE_INPUT_CSS_CLASSES} {BW_DISABLED_DISABLED_INPUTS_CSS_CLASSES} py-2 px-3 "
    # f"pr-11 block w-full shadow-sm text-sm rounded-lg "
    f"block w-full border-gray-200 rounded-md text-sm focus:border-blue-500"
    f" focus:ring-blue-500 "
    f"dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 shadow-sm text-sm"
    f" rounded-lg"
)
BW_PRELINE_INPUT_ERROR_CLASSES = (
    f" border-red-500 text-sm focus:border-red-500 focus:ring-red-500 dark:bg-gray-800 "
    f"dark:border-gray-700 dark:text-gray-400"
)
BW_PRELINE_SELECT_INPUT_CSS_CLASSES = (
    f"{BW_FULL_INPUT_CSS_CLASSES} py-3 px-4 pr-9 block w-full border-gray-200 "
    "rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 "
    "dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400"
)
BW_PRELINE_BASE_BUTTON = (
    f"{BW_BASE_INPUT_CSS_CLASSES} {BW_DISABLED_DISABLED_INPUTS_CSS_CLASSES} inline-flex"
    " justify-center items-center gap-2 rounded-md border border-transparent"
    " transition-all text-sm font-semibold "
)
BW_PRELINE_BASE_TABLE = (
    "table-sort cells-sort min-w-full divide-y divide-gray-200 dark:divide-gray-700"
)
BW_PRELINE_ROUNDED_CLASS = "rounded-full"
BW_PRELINE_BLOCK_CLASS = "w-full"
BW_PRELINE_INPUT_DANGER_STATE = (
    "border-red-500 rounded-md text-sm focus:border-red-500 focus:ring-red-500"
)
BW_PRELINE_INPUT_SUCCESS_STATE = (
    "border-green-500 rounded-md text-sm focus:border-green-500 focus:ring-green-500"
)
BW_PRELINE_FILTER_TEXT_INPUT = (
    f"{BW_FULL_INPUT_CSS_CLASSES} py-2 px-3 pl-11 block w-full border-gray-200 shadow-sm"
    " rounded-md text-sm focus:z-10 focus:border-blue-500 focus:ring-blue-500"
    " dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400"
)
BW_PRELINE_FILTER_SELECT_INPUT_DEFAULT = (
    f"{BW_FULL_INPUT_CSS_CLASSES} py-2 pl-4 pr-0 block w-full border-gray-200 rounded-md"
    " text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-slate-900"
    " dark:border-gray-700 dark:text-gray-400"
)
BW_PRELINE_CHECKBOX_CSS_CLASSES = (
    f"{BW_FULL_INPUT_CSS_CLASSES} shrink-0 mt-0.5 border-gray-200 rounded text-blue-600"
    " pointer-events-none focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700"
    " dark:checked:bg-blue-500 dark:checked:border-blue-500"
    " dark:focus:ring-offset-gray-800"
)
BW_PRELINE_ANCHOR_TAG_DEFAULT_COLOR = (
    "text-blue-600 underline underline-offset-1 decoration-blue-600 hover:opacity-80"
)
BW_PRELINE_DARK_ANCHOR_TAG_DEFAULT_COLOR = (
    "text-gray-800 underline decoration-gray-800 hover:opacity-80 "
    "dark:text-white dark:decoration-white"
)
BW_PRELINE_SECONDARY_ANCHOR_TAG_DEFAULT_COLOR = (
    "text-gray-500 underline decoration-gray-500 hover:opacity-80"
)
BW_PRELINE_PRIMARY_ANCHOR_TAG_DEFAULT_COLOR = (
    "text-blue-600 underline decoration-blue-600 hover:opacity-80"
)
BW_PRELINE_SUCCESS_ANCHOR_TAG_DEFAULT_COLOR = (
    "text-teal-500 underline decoration-teal-500 hover:opacity-80"
)
BW_PRELINE_DANGER_ANCHOR_TAG_DEFAULT_COLOR = (
    "text-red-500 underline decoration-red-500 hover:opacity-80"
)
BW_PRELINE_WARNING_ANCHOR_TAG_DEFAULT_COLOR = (
    "text-yellow-500 underline decoration-yellow-500 hover:opacity-80"
)

BW_PRELINE_CORE_BG_COLORS = {
    "red": {"soft": " bg-red-100 text-red-800 ", "solid": " bg-red-500 text-white "},
    "green": {
        "soft": " bg-green-100 text-green-800 ",
        "solid": " bg-green-500 text-white ",
    },
    "yellow": {
        "soft": " bg-yellow-100 text-yellow-800 ",
        "solid": " bg-yellow-500 text-white ",
    },
    "blue": {"soft": " bg-blue-100 text-blue-800 ", "solid": " bg-blue-500 text-white "},
    "purple": {
        "soft": " bg-purple-100 text-purple-800 ",
        "solid": " bg-purple-500 text-white ",
    },
    "white": {"soft": "bg-white/[.1] text-gray-600", "solid": "bg-white text-gray-600"},
    "indigo": {
        "soft": " bg-indigo-100 text-indigo-800 ",
        "solid": "bg-indigo-500 text-white",
    },
    "gray": {"soft": " bg-gray-100 text-gray-800 ", "solid": " bg-gray-500 text-white "},
}
BW_PRELINE_BASE_BADGE_CLASSES = (
    "uppercase inline-flex items-center gap-1.5 rounded-full font-medium m-0.5"
)
BW_PRELINE_SPAN_TOOLTIP_CSS_CLASSES = (
    "hs-tooltip-content hs-tooltip-shown:opacity-100 hs-tooltip-shown:visible "
    "opacity-0 transition-opacity inline-block absolute invisible z-10 py-1 px-2 "
    "bg-gray-900 text-xs font-medium text-white rounded-md shadow-sm "
    "dark:bg-slate-700"
)
BW_INFO_MODAL_CSS_CLASSES = {
    "client": {
        "cssID": "infoClientModal",
        "tooltip_txt": _(f"What clients are in {BWIdentity.name}"),
    },
    "note": {
        "cssID": "infoNoteModal",
        "tooltip_txt": _(f"What notes are in {BWIdentity.name}"),
    },
    "document": {
        "cssID": "infoDocumentModal",
        "tooltip_txt": _(f"What documents are in {BWIdentity.name}"),
    },
    "job": {
        "cssID": "infoJobModal",
        "tooltip_txt": _(f"What jobs are in {BWIdentity.name}"),
    },
    "task": {
        "cssID": "infoTaskModal",
        "tooltip_txt": _(f"What tasks are in {BWIdentity.name}"),
    },
    "special_assignment": {
        "cssID": "infoSpecialAssignmentModal",
        "tooltip_txt": _(f"What special assignments are in {BWIdentity.name}"),
    },
    "requested_assignment": {
        "cssID": "infoRequestedAssignmentModal",
        "tooltip_txt": _(f"What requested assignments are in {BWIdentity.name}"),
    },
    "client_category": {
        "cssID": "infoClientCategoryModal",
        "tooltip_txt": _(f"What client categories are in {BWIdentity.name}"),
    },
    "job_category": {
        "cssID": "infoJobCategoryModal",
        "tooltip_txt": _(f"What job categories are in {BWIdentity.name}"),
    },
    "bookkeeper": {
        "cssID": "infoBookkeeperModal",
        "tooltip_txt": _(f"What bookkeepers are in {BWIdentity.name}"),
    },
    "assistant": {
        "cssID": "infoAssistantModal",
        "tooltip_txt": _(f"What assistants are in {BWIdentity.name}"),
    },
    "manager": {
        "cssID": "infoManagerModal",
        "tooltip_txt": _(f"What managers are in {BWIdentity.name}"),
    },
    "client_account": {
        "cssID": "infoClientAccountModal",
        "tooltip_txt": _(f"What client accounts are in {BWIdentity.name}"),
    },
    "important_contact": {
        "cssID": "infoImportantContactModal",
        "tooltip_txt": _(f"What important contacts are in {BWIdentity.name}"),
    },
    "discussion": {
        "cssID": "infoDiscussionModal",
        "tooltip_txt": _(f"What discussions are in {BWIdentity.name}"),
    },
    "reports": {
        "cssID": "infoReportsModal",
        "tooltip_txt": _(f"What reports are in {BWIdentity.name}"),
    },
    "site_settings": {
        "cssID": "infoSiteSettingsModal",
        "tooltip_txt": _(f"What site settings are in {BWIdentity.name}"),
    },
}
