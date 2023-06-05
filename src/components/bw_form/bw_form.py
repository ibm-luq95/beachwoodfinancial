# -*- coding: utf-8 -*-#
# In a file called [project root]/components/calendar/calendar.py
from django_components import component


@component.register("bw_form")
class BWForm(component.Component):
    # Templates inside `[your apps]/components` dir and `[project root]/components` dir will be automatically found.
    # To customize which template to use based on context
    # you can override def get_template_name() instead of specifying the below variable.
    template_name = "bw_form/bw_form.html"

    # This component takes one parameter, a date string to show in the template
    def get_context_data(
        self,
        form,
        form_title,
        form_subtitle="",
        form_id="",
        form_method="post",
        form_action_url="",
        is_upload_form=False,
        submit_btn_text="Create",
        perms="",
    ):
        return {
            "form": form,
            "form_subtitle": form_subtitle,
            "form_title": form_title,
            "form_id": form_id,
            "form_method": form_method,
            "form_action_url": form_action_url,
            "is_upload_form": is_upload_form,
            "submit_btn_text": submit_btn_text,
            "perms": perms,
        }

    class Media:
        css = "bw_form/bw_form.css"
        js = "bw_form/bw_form.js"
