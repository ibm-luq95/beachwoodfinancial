# -*- coding: utf-8 -*-#
# In a file called [project root]/components/calendar/calendar.py
from django_components import component


@component.register("dashboard_content_header")
class DashboardContentHeader(component.Component):
    # Templates inside `[your apps]/components` dir and `[project root]/components` dir will be automatically found.
    # To customize which template to use based on context
    # you can override def get_template_name() instead of specifying the below variable.
    template_name = "dashboard_content_header/dashboard_content_header.html"

    # This component takes one parameter, a date string to show in the template
    def get_context_data(self, title, subtitle):
        return {
            "title": title,
            "subtitle": subtitle,
        }

    class Media:
        css = "dashboard_content_header/dashboard_content_header.css"
        js = "dashboard_content_header/dashboard_content_header.js"
