# -*- coding: utf-8 -*-#

from django.urls import path, include

app_name = "beach_wood_users"

urlpatterns = [
    path("auth/", include("beach_wood_user.urls.auth"), name="beach-wood-users-auth-urls"),
]
