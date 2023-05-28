# -*- coding: utf-8 -*-#
# In a file called [project root]/components/calendar/calendar.py
from typing import Optional
from django.utils.translation import gettext as _

from django_components import component


@component.register("tl_create_btn")
class TableListCreateBtn(component.Component):
    # Templates inside `[your apps]/components` dir and `[project root]/components` dir will be automatically found.
    # To customize which template to use based on context
    # you can override def get_template_name() instead of specifying the below variable.
    template_name = "table_list_create_btn/table_list_create_btn.html"

    # This component takes one parameter, a date string to show in the template
    def get_context_data(
        self, app_name: str, end_point_name: Optional[str] = None, btn_txt: str = _("Create")
    ):
        return {"app_name": app_name, "btn_txt": btn_txt, "end_point_name": end_point_name}

    class Media:
        css = "table_list_create_btn/table_list_create_btn.css"
        js = "table_list_create_btn/table_list_create_btn.js"
