# -*- coding: utf-8 -*-#
from django.contrib import admin

from document.models import Document
from core.admin import BWBaseAdminModelMixin


@admin.register(Document)
class DocumentAdmin(BWBaseAdminModelMixin):
    list_display = [
        "title",
        "document_section",
        "status",
        "client",
        "job",
        "task",
        "get_multiple_sections",
        "created_at",
    ]
    list_filter = ["document_section", "status", "client", "job", "task"]

    def get_multiple_sections(self, obj: Document) -> str:
        return str(obj.get_related_objects_as_dict)
        # return format_html(f'<pre><code class="language-json">{obj.get_multiple_sections}</code></pre>')
