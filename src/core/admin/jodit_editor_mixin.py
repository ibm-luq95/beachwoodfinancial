# -*- encoding: utf-8 -*-
from django.contrib import admin
from django.db import models

from core.forms.widgets import RichHTMLEditorWidget


class JoditEditorAdminMixin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {"widget": RichHTMLEditorWidget},
    }

    class Meta:
        abstract = True

    class Media:
        css = {"all": ["css/admin/form_inputs.css", "vendors/jodit/jodit.css"]}
        js = ["vendors/jodit/jodit.min.js", "js/utils/jodit_editor.js"]
