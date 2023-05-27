# -*- coding: utf-8 -*-#
# In a file called [project root]/components/calendar/calendar.py
from django_components import component


@component.register("table_list")
class TableList(component.Component):
    # Templates inside `[your apps]/components` dir and `[project root]/components` dir will be automatically found.
    # To customize which template to use based on context
    # you can override def get_template_name() instead of specifying the below variable.
    template_name = "table_list/table_list.html"

    # This component takes one parameter, a date string to show in the template
    def get_context_data(
        self,
        header_title="",
        header_subtitle="",
        is_pagination_enabled=False,
        objects_list=None,
        header_cols=None,
        perms=None,
        is_show_create_btn=True,
        is_checkbox_enabled=False,
        table_header_columns=None,
    ):
        return {
            "header_title": header_title,
            "header_subtitle": header_subtitle,
            "is_pagination_enabled": is_pagination_enabled,
            "objects_list": objects_list,
            "header_cols": header_cols,
            "perms": perms,
            "is_show_create_btn": is_show_create_btn,
            "is_checkbox_enabled": is_checkbox_enabled,
            "table_header_columns": table_header_columns,
        }

    class Media:
        css = "table_list/table_list.css"
        js = "table_list/table_list.js"
