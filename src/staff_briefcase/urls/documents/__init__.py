# -*- coding: utf-8 -*-#

from django.urls import path, include

app_name = "briefcase_staff_documents"

urlpatterns = [
    path(
        "api/", include("staff_briefcase.urls.documents.api"), name="staff-documents-api"
    ),
]
