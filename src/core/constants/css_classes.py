# -*- coding: utf-8 -*-#
BW_BASE_INPUT_CSS_CLASSES = "bw-input"
BW_DISABLED_ANCHOR_CSS_CLASSES = "bw-disabled-anchor"
BW_DISABLED_DISABLED_INPUTS_CSS_CLASSES = "disabled:opacity-75 cursor-not-allowed"
BW_FULL_INPUT_CSS_CLASSES = (
    f"{BW_BASE_INPUT_CSS_CLASSES} {BW_DISABLED_DISABLED_INPUTS_CSS_CLASSES}"
)
BW_TABLE_LIST_COMPONENT_CLASS = "table-list-component"
BW_TABLE_CONTAINER = "bw-table-container"
BW_TABLE_LIST_SORT_CLASS = "table-sort"
BW_PRELINE_TEXT_INPUT_CSS_CLASSES = (
    f"{BW_BASE_INPUT_CSS_CLASSES} {BW_DISABLED_DISABLED_INPUTS_CSS_CLASSES} py-2 px-3 "
    f"pr-11 block w-full shadow-sm text-sm rounded-lg "
)
BW_PRELINE_BASE_BUTTON = (
    f"{BW_BASE_INPUT_CSS_CLASSES} {BW_DISABLED_DISABLED_INPUTS_CSS_CLASSES} inline-flex justify-center items-center "
    f"gap-2 rounded-md border border-transparent transition-all text-sm font-semibold "
)
BW_PRELINE_BASE_TABLE = (
    "table-sort min-w-full divide-y divide-gray-200 dark:divide-gray-700"
)
BW_PRELINE_ROUNDED_CLASS = "rounded-full"
BW_PRELINE_BLOCK_CLASS = "w-full"
BW_PRELINE_INPUT_DANGER_STATE = (
    "border-red-500 rounded-md text-sm focus:border-red-500 focus:ring-red-500"
)
BW_PRELINE_INPUT_SUCCESS_STATE = (
    "border-green-500 rounded-md text-sm focus:border-green-500 focus:ring-green-500"
)
