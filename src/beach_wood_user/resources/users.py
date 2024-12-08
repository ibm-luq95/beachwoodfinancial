# -*- coding: utf-8 -*-#
from import_export import resources

from beach_wood_user.models import BWUser


class UsersResource(resources.ModelResource):
    class Meta:
        model = BWUser
