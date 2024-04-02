# -*- coding: utf-8 -*-#
from django.urls import path, include

app_name = "staff_briefcase"

urlpatterns = [
    path("", include("staff_briefcase.urls.staff_briefcase"), name="briefcase"),
    path("documents/", include("staff_briefcase.urls.documents"), name="documents"),
]
