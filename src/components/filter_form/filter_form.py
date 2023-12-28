# -*- coding: utf-8 -*-#
# In a file called [project root]/components/calendar/calendar.py
from typing import Optional
from django.utils.translation import gettext as _

from django.forms import Form
from django.urls import reverse_lazy
from django_components import component
import traceback

from core.utils import debugging_print, get_formatted_logger

logger = get_formatted_logger()


@component.register("bw_filter_form")
class BWFilterForm(component.Component):
    # Templates inside `[your apps]/components` dir and `[project root]/components` dir will be automatically found.
    # To customize which template to use based on context
    # you can override def get_template_name() instead of specifying the below variable.
    template_name = "filter_form/filter_form.html"

    # This component takes one parameter, a date string to show in the template
    def get_context_data(
        self,
        filter_form: Form,
        filter_cancel_url: str,
        filter_form_id: Optional[str] = None,
        filter_form_action="",
        is_disabled: bool = False,
        filter_form_method: str = "GET",
        filter_form_title: str = _("Filters"),
    ) -> dict:
        try:
            filter_cancel_url = reverse_lazy(filter_cancel_url)
            if filter_form_action != "":
                filter_form_action = reverse_lazy(filter_form_action)
        except:
            logger.warning(f"{traceback.format_exc()}")
            pass

        return {
            "filter_form": filter_form,
            "filter_cancel_url": filter_cancel_url,
            "filter_form_id": filter_form_id,
            "is_disabled": is_disabled,
            "filter_form_method": filter_form_method,
            "filter_form_title": filter_form_title,
            "filter_form_action": filter_form_action,
        }

    class Media:
        css = "filter_form/filter_form.css"
        js = "filter_form/filter_form.js"
