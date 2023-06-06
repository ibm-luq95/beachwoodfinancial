# -*- coding: utf-8 -*-#
from django.contrib import admin

from important_contact.models import ImportantContact
from core.admin import BWBaseAdminModelMixin


@admin.register(ImportantContact)
class ImportantContactAdmin(BWBaseAdminModelMixin):
    pass
