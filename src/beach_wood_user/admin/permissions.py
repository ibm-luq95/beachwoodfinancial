# -*- coding: utf-8 -*-#
from django.contrib import admin
from django.contrib.auth.models import Permission


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    pass
