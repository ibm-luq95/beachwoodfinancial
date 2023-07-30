# -*- coding: utf-8 -*-#
from datetime import datetime

from django import template
from django.utils.translation import gettext as _

from core.utils import get_request_context, debugging_print

register = template.Library()


@register.inclusion_tag("bw_ui_components/elements/date.html", takes_context=True)
def bw_date(context, *args, **kwargs) -> dict:
    context_data = get_request_context(context, kwargs)
    # US style mm/dd/yyyy, h:i format;. e.g (12/28/2023). Can use "/" or "-"
    only_date_format = "%m/%d/%Y"
    date_time_format = "%m/%d/%Y, %H:%M"
    date_txt: datetime = kwargs.get("date_txt", None)
    date_format = kwargs.get("date_format", None)
    show_time = kwargs.get("show_time", False)
    is_in_table_list = kwargs.get("is_in_table_list", False)
    show_no_date_tooltip = kwargs.get("show_no_date_tooltip", False)

    if date_txt == "":
        new_formatted_date = "---"
        show_no_date_tooltip = _("No date available")
    else:
        if date_format is not None:
            new_formatted_date = date_txt.strftime(date_format)
        else:
            new_formatted_date = date_txt.strftime(only_date_format)
            if show_time is True:
                new_formatted_date = date_txt.strftime(date_time_format)

    kwargs.update(
        {
            "is_in_table_list": is_in_table_list,
            "date_txt": date_txt,
            "show_time": show_time,
            "formatted_date": new_formatted_date,
            "show_no_date_tooltip": show_no_date_tooltip,
        }
    )
    return {**context_data, **kwargs}
