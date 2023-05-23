# -*- coding: utf-8 -*-#
from typing import Optional

from django.forms import BoundField

import stringcase

from core.utils import debugging_print

BW_TAILWIDCSS_TEXT_INPUT_CSS_CLASSES = (
    "py-2 px-3 pr-11 block w-full border-gray-200 shadow-sm text-sm rounded-lg "
    "focus:border-blue-500 focus:ring-blue-500 dark:bg-slate-900 "
    "dark:border-gray-700 dark:text-gray-400"
)


def bw_render_form_field(form_input: BoundField, attributes: Optional[dict] = None):
    form_field = form_input.field
    new_attrs = {
        "class": BW_TAILWIDCSS_TEXT_INPUT_CSS_CLASSES,
        # "id": f"id_{form_input.label.lower().replace(" ", "-")}"
    }
    if attributes is not None:
        new_attrs.update(attributes)
    widget = form_input.as_widget(attrs=new_attrs)
    return widget
