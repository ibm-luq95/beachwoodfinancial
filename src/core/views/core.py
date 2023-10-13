# -*- coding: utf-8 -*-#
import json

from django.conf import settings
from django.http import HttpResponse
from django.template import Template, Context
from django.urls import reverse_lazy

JS_SETTINGS_TEMPLATE = """
window.settings = JSON.parse('{{ json_data|escapejs }}');
"""


# @cache_page(60 * 15)
def js_settings(request):
    data = {
        # "MEDIA_URL": settings.MEDIA_URL,
        # "STATIC_URL": settings.STATIC_URL,
        "DEBUG": settings.DEBUG,
        "FETCHURLNAMEURL": str(reverse_lazy("core:api:fetch-url")),
        "CURRENTUSER": str(request.user.pk),
        # "LANGUAGES": settings.LANGUAGES,
        # "DEFAULT_LANGUAGE_CODE": settings.LANGUAGE_CODE,
        # "CURRENT_LANGUAGE_CODE": request.LANGUAGE_CODE,
    }
    json_data = json.dumps(data)
    template = Template(JS_SETTINGS_TEMPLATE)
    context = Context({"json_data": json_data})
    response = HttpResponse(
        content=template.render(context),
        content_type="application/javascript; charset=UTF-8",
    )
    return response
