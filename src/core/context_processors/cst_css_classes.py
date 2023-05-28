# -*- coding: utf-8 -*-#
def access_css_classes_constants(request) -> dict:
    return {
        "BW_TAILWINDCSS_TEXT_INPUT_CSS_CLASSES": (
            "py-2 px-3 pr-11 block w-full border-gray-200 shadow-sm text-sm rounded-lg "
            "focus:border-blue-500 focus:ring-blue-500 dark:bg-slate-900 "
            "dark:border-gray-700 dark:text-gray-400"
        ),
        "BW_TAILWINDCSS_TABLE_CSS_CLASSES": "table-sort min-w-full divide-y divide-gray-200 dark:divide-gray-700",
        "BW_BASE_INPUT_CSS_CLASSES": "bw-input",
        "BW_DISABLED_ANCHOR_CSS_CLASSES": "bw-disabled-anchor",
        "BW_DISABLED_DISABLED_INPUTS_CSS_CLASSES": "disabled:opacity-75 cursor-not-allowed",
    }
