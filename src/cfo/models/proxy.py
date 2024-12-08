# -*- coding: utf-8 -*-#
from cfo.models.cfo import CFO


class CFOProxy(CFO):

    class Meta(CFO.Meta):
        proxy = True
