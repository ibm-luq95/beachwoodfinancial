# -*- coding: utf-8 -*-#
from .assistant import Assistant


class AssistantProxy(Assistant):
    class Meta:
        proxy = True
