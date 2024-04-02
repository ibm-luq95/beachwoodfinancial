# -*- coding: utf-8 -*-#

from django.urls import path, include

app_name = "briefcase_staff_accounts"

urlpatterns = [
    path("api/", include("staff_briefcase.urls.accounts.api"), name="staff-accounts-api"),
]
