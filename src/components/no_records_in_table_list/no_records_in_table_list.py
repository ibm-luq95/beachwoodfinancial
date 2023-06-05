# -*- coding: utf-8 -*-#
# In a file called [project root]/components/calendar/calendar.py
from django_components import component


@component.register("no_records")
class NoRecords(component.Component):
    # Templates inside `[your apps]/components` dir and `[project root]/components` dir will be automatically found.
    # To customize which template to use based on context
    # you can override def get_template_name() instead of specifying the below variable.
    template_name = "no_records_in_table_list/no_records_in_table_list.html"

    # This component takes one parameter, a date string to show in the template
    def get_context_data(self, msg, app_name):
        return {"msg": msg, "app_name": app_name}

    class Media:
        css = "no_records_in_table_list/no_records_in_table_list.css"
        js = "no_records_in_table_list/no_records_in_table_list.js"
