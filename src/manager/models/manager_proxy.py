# -*- coding: utf-8 -*-#
from .manager import Manager


class ManagerProxy(Manager):
    class Meta(Manager.Meta):
        proxy = True
