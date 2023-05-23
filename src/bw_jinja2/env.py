# -*- coding: utf-8 -*-#
from crispy_forms.templatetags import crispy_forms_tags
from crispy_tailwind.templatetags import tailwind_filters
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse

from jinja2 import Environment, Undefined, FileSystemLoader, PackageLoader
from webpack_boilerplate.contrib.jinja2ext import stylesheet_pack, javascript_pack
from webpack_boilerplate.templatetags import webpack_loader
from widget_tweaks.templatetags import widget_tweaks

from core.templatetags.core_tags import show_crispy_form
from core.templatetags.forms_tags import bw_render_form_field


# for more later django installations use:
# from django.templatetags.static import static


class SilentUndefined(Undefined):
    def _fail_with_undefined_error(self, *args, **kwargs):
        return ""


class JinjaEnvironment(Environment):
    def __init__(self, **kwargs):
        super(JinjaEnvironment, self).__init__(**kwargs)
        # self.globals["undefined"] = SilentUndefined
        self.globals["static"] = staticfiles_storage.url
        self.globals["url"] = reverse
        self.globals["webpack_loader"] = webpack_loader
        self.globals["stylesheet_pack"] = stylesheet_pack
        self.globals["javascript_pack"] = javascript_pack
        self.globals["crispy"] = show_crispy_form
        self.globals["tailwind_filters"] = tailwind_filters
        self.globals["widget_tweaks"] = widget_tweaks
        self.globals["bw_render_form_field"] = bw_render_form_field
        # self.globals["forms"] = self.make_globals("macros/core")
        # self.globals["loader"] = FileSystemLoader(
        #     settings.BASE_DIR / "templates"
        # )
        # global_context = self.get_template("macros/dashboard/content_header.jinja").make_globals()
        # self.globals.update(global_context)
        # print(self.list_templates())
