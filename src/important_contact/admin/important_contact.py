# -*- coding: utf-8 -*-#
from django.contrib import admin

from important_contact.models import ImportantContact
from core.admin import BWBaseAdminModelMixin


@admin.register(ImportantContact)
class ImportantContactAdmin(BWBaseAdminModelMixin):
    list_display = [
        "get_client",
        "contact_label",
        "company_name",
        "contact_first_name",
        "contact_last_name",
    ]

    def get_client(self, obj: ImportantContact):
        return obj.client.get().name
