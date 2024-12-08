# -*- coding: utf-8 -*-#
from import_export import resources

from assistant.models import AssistantProxy


class AssistantResource(resources.ModelResource):
    class Meta:
        model = AssistantProxy
