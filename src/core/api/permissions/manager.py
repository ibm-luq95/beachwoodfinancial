# -*- coding: utf-8 -*-#
from rest_framework import permissions


class ManagerApiPermission(permissions.BasePermission):
    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        # from pprint import pprint
        # pprint(request.user.has_perm("bookkeeper.bookkeeper_user"))
        # print(bool(request.user and request.user.is_staff))
        if request.user.user_type == "manager" or request.user.user_type == "assistant":
            return True
